import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()
in_path = filedialog.askopenfilename()

tkinter.Tk().withdraw()
out_path = filedialog.asksaveasfilename()

context_free_grammar=nltk.data.load('English_Grammar.cfg')

f1=open(in_path,'r')

grammatically_correct_sentences=[]
grammatically_incorrect_sentences=[]
ambiguous_sentences=[]

parser = nltk.ChartParser(context_free_grammar)

for text in f1:

	sentences=sent_tokenize(text)

	for j in sentences:

		parse_tree_count=0

		filtered_sentence=j.replace('.','')

		filtered_sentence=filtered_sentence.lower()

		word_tokens=word_tokenize(filtered_sentence)

		parse_tree=parser.parse(word_tokens)

		for tree in parse_tree:

			parse_tree_count=parse_tree_count+1

		if(parse_tree_count==0):

			grammatically_incorrect_sentences.append(j)

		elif(parse_tree_count==1):

			grammatically_correct_sentences.append(j)

		else:

			grammatically_correct_sentences.append(j)
			ambiguous_sentences.append(j)

f2=open(out_path,"w")

f2.write ("*****Grammatically Correct Sentences*****\n\n")
	
for i in grammatically_correct_sentences:

	f2.write(i)
	f2.write("\n")

f2.write ("\n*****Grammatically Incorrect Sentences*****\n\n")

for i in grammatically_incorrect_sentences:

	f2.write(i)
	f2.write("\n")

f2.write ("\n*****Ambiguous Sentences*****\n\n")

for i in ambiguous_sentences:

	f2.write(i)
	f2.write("\n")

f1.close()
f2.close()
