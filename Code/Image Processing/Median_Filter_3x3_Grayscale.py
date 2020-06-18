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

#Order Statistic Filters / Rank Order Filters

#1) Median Filter with 3x3 mask

#Let us assume 3x3 mask. The pixel values are aranged in ascending order. Median filter sorts the list and finds the median. Then, the centre pixel is replaced by the median value.

#Steps :
#1) Read all the pixel values in the selected window.
#2) Sort the values in ascending order.
#3) Choose the median, that is , the central value.
#4) This value replaces the central pixel of the mask.
#5) Then, move the window by one pixel and repeat the process until the entire image is processed.
#6) Outer rows and columns are not affected by this process.

for i in range(0,rows):
	for j in range(0,columns):
		
		#Outer rows and columns are not affected by this process.
		if((i!=0)and(i!=rows-1)and(j!=0)and(j!=columns-1)):

			mask_array=[]
		
			#Read all the pixel values in the selected window.
			for m in range(-1,2):

				for n in range(-1,2):

					mask_array.append(gray[i+m,j+n])

			#Mask of size 3x3
			l=len(mask_array)

			#Sort the values in ascending order.
			#Sorting using Bubble Sort in Ascending Order
			for m in range(0,l):

				for n in range(0,l-m-1):

					if(mask_array[n]>mask_array[n+1]):

						temp=mask_array[n]
						mask_array[n]=mask_array[n+1]
						mask_array[n+1]=temp

			#The centre pixel is replaced by the median value

			output[i,j]=mask_array[4]
    

while(1):

		cv2.imshow('Median Filter Image',output)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

Tkinter.Tk().withdraw() # Close the root window
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,output)
