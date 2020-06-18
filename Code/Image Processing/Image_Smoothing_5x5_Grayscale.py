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

#Smoothing Filter

#Smoothing filters are used for blurring and for noise reduction. Blurring is removal of small details from an image.

#The output (response) of a smoothing, linear spatial filter is simply the average of the pixels contained in the neighborhood of the filter mask. These filters sometimes are called averaging filters. They also are referred to a lowpass filters.

#The idea behind smoothing filters is replacing the value of every pixel in an image by the average of the intensity levels in the neighborhood defined by the filter mask.

#An m * n mask would have a normalizing constant equal to 1/mn. A spatial averaging filter in which all coefficients are equal sometimes is called a box filter.

#This process results in an image with reduced "sharp" transitions in intensities. Because random noise typically consists of sharp transitions in intensity levels, the most obvious application of smoothing is noise reduction.

#However, edges (which almost always are desirable features of an image) also are characterized by sharp intensity transitions, so averaging filters have the undesirable side effect that they blur edges.

for i in range(0,rows):
	for j in range(0,columns):
		
		#Outer rows and columns are not affected by this process.
		if((i>1)and(i<rows-2)and(j>1)and(j<columns-2)):

			mask_array=[]
			total_sum=0
		
			#Read all the pixel values in the selected window.
			for m in range(-2,3):

				for n in range(-2,3):

					mask_array.append(gray[i+m,j+n])

			#Mask of size 5x5
			l=len(mask_array)

			for m in range(0,l):

				total_sum=total_sum+mask_array[m]

			average=int(round(float(total_sum)/25))

			#The centre pixel is replaced by the average value

			output[i,j]=average
    

while(1):

		cv2.imshow('Smoothing Filter Image',output)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

Tkinter.Tk().withdraw() # Close the root window
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,output)
