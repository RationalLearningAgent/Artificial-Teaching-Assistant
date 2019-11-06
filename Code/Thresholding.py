import cv2
import numpy as np
import Tkinter
import tkFileDialog

Tkinter.Tk().withdraw() # Close the root window
in_path = tkFileDialog.askopenfilename()

#RGB Image

img = cv2.imread(in_path)
	
print "RGB Image Shape is :",img.shape

while(1):

		cv2.imshow('RGB Image',img)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

#Converting RGB Image to Gray Scale Image

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print "Gray Scale Image Shape is :",gray.shape

while(1):

		cv2.imshow('Gray Scale Image',gray)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

#Getting the shape of the image

shape_tuple=gray.shape
rows=shape_tuple[0]
columns=shape_tuple[1]

rows,colums=gray.shape

#Zero Memory point operations

#1) Thresholding

T=input("Enter the Threshold Value T : ")

for i in range(0,rows):
	for j in range(0,columns):
		
		if(gray[i,j]>T):
			
			gray[i,j]=256-1

		else:

			gray[i,j]=0
    

while(1):

		cv2.imshow('Threshold Image',gray)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

Tkinter.Tk().withdraw() # Close the root window
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,gray)
