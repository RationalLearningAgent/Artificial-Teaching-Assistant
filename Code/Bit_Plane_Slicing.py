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

output=[[[0 for i in range(0,8)] for j in range(0,columns)] for k in range(0,rows)]

#Convert grayscale value into binary
for i in range(0,rows):

	for j in range(0,columns):

		number=gray[i,j]

		for k in range(0,8):

			quotient=number/2

			output[i][j][k]=number-2*quotient

			number=quotient















#LSB : Bit Plane 0
bit_plane_0 = np.zeros((rows,columns),np.uint8)

for i in range(0,rows):

	for j in range(0,columns):

		value=output[i][j][0]

		if(value==1):
	
			bit_plane_0[i][j]=255

		else:

			bit_plane_0[i][j]=0

while(1):

		cv2.imshow('LSB : Bit Plane 0',bit_plane_0)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break


















#Bit Plane 1
bit_plane_1 = np.zeros((rows,columns),np.uint8)

for i in range(0,rows):

	for j in range(0,columns):

		value=output[i][j][1]

		if(value==1):
	
			bit_plane_1[i][j]=255

		else:

			bit_plane_1[i][j]=0

while(1):

		cv2.imshow('Bit Plane 1',bit_plane_1)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break




















#Bit Plane 2
bit_plane_2 = np.zeros((rows,columns),np.uint8)

for i in range(0,rows):

	for j in range(0,columns):

		value=output[i][j][2]

		if(value==1):
	
			bit_plane_2[i][j]=255

		else:

			bit_plane_2[i][j]=0

while(1):

		cv2.imshow('Bit Plane 2',bit_plane_2)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break




















#Bit Plane 3
bit_plane_3 = np.zeros((rows,columns),np.uint8)

for i in range(0,rows):

	for j in range(0,columns):

		value=output[i][j][3]

		if(value==1):
	
			bit_plane_3[i][j]=255

		else:

			bit_plane_3[i][j]=0

while(1):

		cv2.imshow('Bit Plane 3',bit_plane_3)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break






















#Bit Plane 4
bit_plane_4 = np.zeros((rows,columns),np.uint8)

for i in range(0,rows):

	for j in range(0,columns):

		value=output[i][j][4]

		if(value==1):
	
			bit_plane_4[i][j]=255

		else:

			bit_plane_4[i][j]=0

while(1):

		cv2.imshow('Bit Plane 4',bit_plane_4)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break


















































#Bit Plane 5
bit_plane_5 = np.zeros((rows,columns),np.uint8)

for i in range(0,rows):

	for j in range(0,columns):

		value=output[i][j][5]

		if(value==1):
	
			bit_plane_5[i][j]=255

		else:

			bit_plane_5[i][j]=0

while(1):

		cv2.imshow('Bit Plane 5',bit_plane_5)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break




































#Bit Plane 6
bit_plane_6 = np.zeros((rows,columns),np.uint8)

for i in range(0,rows):

	for j in range(0,columns):

		value=output[i][j][6]

		if(value==1):
	
			bit_plane_6[i][j]=255

		else:

			bit_plane_6[i][j]=0

while(1):

		cv2.imshow('Bit Plane 6',bit_plane_6)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break



























#MSB : Bit Plane 7
bit_plane_7 = np.zeros((rows,columns),np.uint8)

for i in range(0,rows):

	for j in range(0,columns):

		value=output[i][j][7]

		if(value==1):
	
			bit_plane_7[i][j]=255

		else:

			bit_plane_7[i][j]=0

while(1):

		cv2.imshow('MSB : Bit Plane 7',bit_plane_7)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break





























