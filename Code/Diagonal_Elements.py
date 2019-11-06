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

output=np.zeros((rows,columns),np.uint8)

for i in range(0,rows):
	for j in range(0,columns):
		
		#Outer rows and columns are not affected by this process.
		if((i!=0)and(i!=rows-1)and(j!=0)and(j!=columns-1)):

			discrete_laplacian=int(gray[i-1,j-1])+int(gray[i-1,j])+int(gray[i-1,j+1])+int(gray[i,j-1])+int(gray[i,j+1])+int(gray[i+1,j-1])+int(gray[i+1,j])+int(gray[i+1,j+1])-8*int(gray[i,j])


			value=int(gray[i,j])+-1*discrete_laplacian

			if(value>255):
		
				output[i,j]=255

			elif(value<0):

				output[i,j]=0

			else:

				output[i,j]=value

while(1):

		cv2.imshow('Sharpening Filter Image',output)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

Tkinter.Tk().withdraw() # Close the root window
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,output)
