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

#Getting the shape of the image

shape_tuple=img.shape
rows=shape_tuple[0]
columns=shape_tuple[1]

output=np.zeros((rows,columns,3),np.uint8)


for k in range(0,3):

	for i in range(0,rows):
		for j in range(0,columns):
		
			#Outer rows and columns are not affected by this process.
			if((i!=0)and(i!=rows-1)and(j!=0)and(j!=columns-1)):

				discrete_laplacian=int(img[i-1,j-1,k])+int(img[i-1,j,k])+int(img[i-1,j+1,k])+int(img[i,j-1,k])+int(img[i,j+1,k])+int(img[i+1,j-1,k])+int(img[i+1,j,k])+int(img[i+1,j+1,k])-8*int(img[i,j,k])


				value=int(img[i,j,k])+-1*discrete_laplacian

				if(value>255):
		
					output[i,j,k]=255

				elif(value<0):

					output[i,j,k]=0

				else:

					output[i,j,k]=value

while(1):

		cv2.imshow('Sharpening Filter Image',output)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

Tkinter.Tk().withdraw() # Close the root window
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,output)
