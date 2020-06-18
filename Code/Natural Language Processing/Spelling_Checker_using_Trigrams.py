import json

from nltk.tokenize import word_tokenize

from nltk.corpus import words

from nltk.corpus import brown,gutenberg,webtext,reuters,inaugural

from nltk import bigrams,trigrams

from nltk.metrics import edit_distance

import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()
in_path = filedialog.askopenfilename()

tkinter.Tk().withdraw()
out_path = filedialog.asksaveasfilename()

try:

	trigram_model=json.load(open("Spelling_Correction/trigrams.txt"))

except IOError:

	corpus=[brown,gutenberg,webtext,reuters,inaugural]

	trigram_model={}

	for i in corpus:

		for sentence in i.sents():

			for w1,w2,w3 in trigrams(sentence):

				if str((w1,w2)) in trigram_model:

					if w3 in trigram_model[str((w1,w2))].keys():

						trigram_model[str((w1,w2))][w3]=trigram_model[str((w1,w2))][w3]+1

					else:

						trigram_model[str((w1,w2))][w3] = 1

				else:

					trigram_model[str((w1,w2))] = {}

					trigram_model[str((w1,w2))][w3] = 1

	json.dump(trigram_model,open("Spelling_Correction/trigrams.txt",'w'))


f1=open(in_path,"r")
f2=open(out_path,"w")

for text in f1:

	t=[]

	abc=trigrams(word_tokenize(text))

	for w1, w2, w3 in abc:

		if str((w1,w2)) in trigram_model:

			l=list(trigram_model[str((w1,w2))].keys())

		else:

			l=[]
	
		length=len(l)

		if((length!=0)and(w3.lower() not in words.words())):

			minimum=edit_distance(w3,l[0])
			min_key=l[0]
	
			for i in range(1,length):

				key=l[i]

				b=edit_distance(w3,key)

				if(b<minimum):

					min_key=key
					minimum=b

			if(len(t)==0):
	
				t.append(w1)
				t.append(w2)
				t.append(min_key)

			else:
	
				t.append(min_key)

		else:

			if(len(t)==0):
	
				t.append(w1)
				t.append(w2)
				t.append(w3)

			else:

				t.append(w3)
	
	str1=' '.join(t)

	f2.write (str1)

f1.close()
f2.close()

