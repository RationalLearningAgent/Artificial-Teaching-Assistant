from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.corpus import twitter_samples
from nltk import FreqDist, classify, NaiveBayesClassifier
import re, string, random
import pickle

import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()
in_path = filedialog.askopenfilename()

tkinter.Tk().withdraw()
out_path = filedialog.asksaveasfilename()

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens




def get_all_words(cleaned_tokens_list):
	for tokens in cleaned_tokens_list:
		for token in tokens:
			yield token




def get_tweets_for_model(cleaned_tokens_list):
	for tweet_tokens in cleaned_tokens_list:
		yield dict([token, True] for token in tweet_tokens)



saved_model_path = 'Sentiment_Analysis/Sentiment_Analysis_Trained_Model.sav'

try:

	classifier = pickle.load(open(saved_model_path, 'rb'))

except IOError:


	positive_tweets = twitter_samples.strings('positive_tweets.json')
	negative_tweets = twitter_samples.strings('negative_tweets.json')
	text = twitter_samples.strings('tweets.20150430-223406.json')

	stop_words = stopwords.words('english')
    
	tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]
	positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
	negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')





	positive_cleaned_tokens_list = []
	negative_cleaned_tokens_list = []

	for tokens in positive_tweet_tokens:
		positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

	for tokens in negative_tweet_tokens:
		negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

	all_pos_words = get_all_words(positive_cleaned_tokens_list)












	positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
	negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

	positive_dataset = [(tweet_dict, "Positive") for tweet_dict in positive_tokens_for_model]

	negative_dataset = [(tweet_dict, "Negative") for tweet_dict in negative_tokens_for_model]

	dataset = positive_dataset + negative_dataset











	#Train the Model

	random.shuffle(dataset)

	train_data = dataset[:7000]

	classifier = NaiveBayesClassifier.train(train_data)

	pickle.dump(classifier, open(saved_model_path, 'wb'))

    










#Process the input file

f1=open(in_path,"r")
f2=open(out_path,"w")

positive_sentiments=[]
negative_sentiments=[]

for i in f1:

	student_feedback=i

	student_feedback = student_feedback.replace("\n","")

	student_feedback_tokens = remove_noise(word_tokenize(student_feedback))

	sentiment=classifier.classify(dict([token, True] for token in student_feedback_tokens))

	if sentiment=="Positive":

		positive_sentiments.append(student_feedback)

	else:

		negative_sentiments.append(student_feedback)


f2.write("Total no of Student Feedbacks : "+str(len(positive_sentiments)+len(negative_sentiments)))
f2.write("\nTotal no of Positive Student Feedbacks : "+str(len(positive_sentiments)))
f2.write("\nTotal no of Negative Student Feedbacks : "+str(len(negative_sentiments)))

f2.write ("\n\n*****Positive Student Feedbacks*****\n\n")
	
for i in positive_sentiments:

	f2.write(i)
	f2.write("\n")

f2.write ("\n*****Negative Student Feedbacks*****\n\n")

for i in negative_sentiments:

	f2.write(i)
	f2.write("\n")

