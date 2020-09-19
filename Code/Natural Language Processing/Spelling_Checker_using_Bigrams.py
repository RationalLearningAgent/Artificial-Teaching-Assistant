import json

from nltk.tokenize import word_tokenize

from nltk.corpus import words

from nltk.corpus import brown

from nltk import bigrams

from nltk.metrics import edit_distance

import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()
in_path = filedialog.askopenfilename()

tkinter.Tk().withdraw()
out_path = filedialog.asksaveasfilename()

try:

	bigram_model=json.load(open("Spelling_Correction/bigrams.txt"))

except IOError:

	bigram_model={}

	for sentence in brown.sents():

		for w1,w2 in bigrams(sentence):

			if w1 in bigram_model:

				if w2 in bigram_model[w1].keys():

					bigram_model[w1][w2]=bigram_model[w1][w2]+1

				else:

					bigram_model[w1][w2] = 1

			else:

				bigram_model[w1] = {}

				bigram_model[w1][w2] = 1

	json.dump(bigram_model,open("Spelling_Correction/bigrams.txt",'w'))

f1=open(in_path,"r")
f2=open(out_path,"w")

for text in f1:

	t=[]

	abc=bigrams(word_tokenize(text))

	for w1,w2 in abc:

		if w1 in bigram_model:

			l=list(bigram_model[w1].keys())

		else:

			l=[]
	
		length=len(l)

		if((length!=0)and(w2.lower() not in words.words())):

			minimum=edit_distance(w2,l[0])
			min_key=l[0]
	
			for i in range(1,length):

				key=l[i]

				b=edit_distance(w2,key)

				if(b<minimum):

					min_key=key
					minimum=b

			if(len(t)==0):
	
				t.append(w1)
				t.append(min_key)

			else:
	
				t.append(min_key)

		else:

			if(len(t)==0):
	
				t.append(w1)
				t.append(w2)

			else:

				t.append(w2)
	
	str1=' '.join(t)

	f2.write (str1)

f1.close()
f2.close()

