import cv2
import numpy as np
import Tkinter
import tkFileDialog

#Take image path through Tkinter

Tkinter.Tk().withdraw()
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

#Getting the shape of the image

shape_tuple=img.shape
rows=shape_tuple[0]
columns=shape_tuple[1]

output = np.zeros((rows,columns,3),np.uint8)

#Performing Histogram Equalization of the Image

for k in range(0,3):

	gray_levels=[i for i in range(0,256)]
	no_of_pixels=[0 for i in range(0,256)]

	for i in range(0,rows):

		for j in range(0,columns):

			no_of_pixels[img[i,j,k]]=no_of_pixels[img[i,j,k]]+1

	#Probability Density Function (PDF)

	total_no_of_pixels=rows*columns

	probability_distribution_function=[0.0 for i in range(0,256)]

	for i in range(0,256):

		probability_distribution_function[i]=float(no_of_pixels[i])/total_no_of_pixels

	#Cumulative Distribution Function (CDF)

	cumulative_distribution_function=[0.0 for i in range(256)]

	cumulative_distribution_function[0]=probability_distribution_function[0]

	for i in range(1,256):

		cumulative_distribution_function[i]=cumulative_distribution_function[i-1]+probability_distribution_function[i]

	#Multiply the CDF value by the maximum gray level value

	equalize=[0.0 for i in range(0,256)]

	for i in range(0,256):

		equalize[i]=cumulative_distribution_function[i]*255

	#Round off to the nearest gray level

	rounding_off=[0 for i in range(0,256)]

	for i in range(0,256):

		rounding_off[i]=int(round(equalize[i]))

	#Generate the Equalized Histogram Image

	for i in range(0,rows):

		for j in range(0,columns):

			output[i,j,k]=rounding_off[img[i,j,k]]



while(1):

	cv2.imshow('Histogram Equalization Image',output)

	c = cv2.waitKey(1)
	
	if c == 27:
		cv2.destroyAllWindows()
		break

#Saving Histogram Equalized Image

Tkinter.Tk().withdraw()
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,output)

