from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()
in_path = filedialog.askopenfilename()

tkinter.Tk().withdraw()
out_path = filedialog.asksaveasfilename()

#The input text

f1=open(in_path,"r")
input_text=f1.read()

processed_text = input_text.replace("\n","")

text=processed_text

#Step 1 : Create Word Frequency Table

frequency_table=dict()

stop_words=stopwords.words("english")
ps=PorterStemmer()

text=text.lower()

words=word_tokenize(text)

#Remove Special Characters

special_characters=["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]",":",";",'"',"'","|","\a","<",",",">",".","?","/"]

words_filtered1=[]

for i in words:

	if i not in special_characters:

		words_filtered1.append(i)

#Remove Stop Words

word_tokens=[]

for i in words_filtered1:

	if i not in stop_words:

		word_tokens.append(i)

#Frequency Table

for i in word_tokens:

	word_stem=ps.stem(i)

	if word_stem in frequency_table:

		frequency_table[word_stem]=frequency_table[word_stem]+1

	else:

		frequency_table[word_stem]=1






#Step 2 : Sentence Tokenization

sentences=sent_tokenize(text)




#Step 3 : Calculate Sentence Score

no_of_sentences=len(sentences)

sentence_value=[0 for i in range(0,no_of_sentences)]

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
		

	


	for j in frequency_table:

		if j in token3:

			sentence_value[i]=sentence_value[i]+frequency_table[j]

	sentence_value[i]=sentence_value[i]/no_of_important_words_in_sentence







#Step 4 : Find the threshold

sum=0

for i in sentence_value:

	sum=sum+i

threshold=sum/len(sentence_value)









#Step 5 : Generate the Summary

f2=open(out_path,"w")

processed_text_sentences=sent_tokenize(processed_text)

#value=float(input("Enter the Percentage of Summarization : "))

value=100

value=value/100;

for i in range(0,no_of_sentences):

	if(sentence_value[i]>threshold*value):

		f2.write (processed_text_sentences[i])			

	
	
	







		

