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

#Convert image to grayscale

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Getting the shape of the image

shape_tuple=img.shape
rows=shape_tuple[0]
columns=shape_tuple[1]

output=np.zeros((rows,columns,3),np.uint8)

r1=input("Enter the value of r1 : ")
r2=input("Enter the value of r2 : ")

red_value=input("\nEnter the R value : ")
green_value=input("Enter the G value : ")
blue_value=input("Enter the B value : ")

for i in range(0,rows):
	for j in range(0,columns):
		
		if((r1<=gray[i,j])and(gray[i,j]<=r2)):
			
			output[i,j,0]=blue_value
			output[i,j,1]=green_value
			output[i,j,2]=red_value
		
		else:

			output[i,j]=img[i,j]

while(1):

		cv2.imshow('Change RGB Image Text Colour',output)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

Tkinter.Tk().withdraw() # Close the root window
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,output)	
