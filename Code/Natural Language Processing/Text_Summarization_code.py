#Extractive Text Summarization using NLTK

#importing libraries
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

import tkinter
from tkinter import filedialog

#Getting input file path from the user
tkinter.Tk().withdraw()
in_path = filedialog.askopenfilename()

#Getting output file path from the user
tkinter.Tk().withdraw()
out_path = filedialog.asksaveasfilename()

#The input text
f1=open(in_path,"r")
input_text=f1.read()

#Removing newline character \n from the input
processed_text = input_text.replace("\n","")

text=processed_text

#Getting all English stopwords from nltk library
stop_words=stopwords.words("english")

ps=PorterStemmer()

text=text.lower()

#Word Tokenization
words=word_tokenize(text)

#Remove Special Characters

special_characters=["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]",":",";",'"',"'","|","\a","<",",",">",".","?","/"]

words_filtered1=[]

for i in words:

	if i not in special_characters:

		words_filtered1.append(i)

#Remove Stop Words

words_filtered2=[]

for i in words_filtered1:

	if i not in stop_words:

		words_filtered2.append(i)

#Creating the Text Words Frequency Table

textwords_frequency_table=dict()

for i in words_filtered2:

	word_stem=ps.stem(i)

	if word_stem in textwords_frequency_table:

		textwords_frequency_table[word_stem]=textwords_frequency_table[word_stem]+1

	else:

		textwords_frequency_table[word_stem]=1

#Sentence Tokenization
sentences=sent_tokenize(text)

#Calculating Sentence Importance

no_of_sentences=len(sentences)

#Initialising importance value of each sentence with 0
sentence_value=[0 for i in range(0,no_of_sentences)]

#Calculating importance value of each sentence of the text
for i in range(0,no_of_sentences):

	token1=word_tokenize(sentences[i])

	token2=[]

	for j in token1:

		if j not in special_characters:

			token2.append(j)

	token3=[]

	for j in token2:

		if j not in stop_words:

			token3.append(j)

	no_of_important_words_in_sentence=len(token3)

	for j in range(0,len(token3)):

		token3[j]=ps.stem(token3[j])
			
	for j in textwords_frequency_table:

		if j in token3:

			sentence_value[i]=sentence_value[i]+textwords_frequency_table[j]

	sentence_value[i]=sentence_value[i]/no_of_important_words_in_sentence

#Finding the Sentence Acceptance Value

sum=0

for i in sentence_value:

	sum=sum+i

value=(sum/len(sentence_value))*1.3

#Generating the Summary and saving it in output file
f2=open(out_path,"w")

processed_text_sentences=sent_tokenize(processed_text)

#Taking the percentage of summarization from the user
percentage_of_summarization=float(input("Enter the Percentage of Summarization : "))

percentage_of_summarization=percentage_of_summarization/100;

for i in range(0,no_of_sentences):

	if(sentence_value[i]>value*percentage_of_summarization):

		f2.write (processed_text_sentences[i])			

