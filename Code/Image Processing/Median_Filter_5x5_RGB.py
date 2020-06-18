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

#Order Statistic Filters / Rank Order Filters

#1) Median Filter with 5x5 mask

#Let us assume 3x3 mask. The pixel values are aranged in ascending order. Median filter sorts the list and finds the median. Then, the centre pixel is replaced by the median value.

#Steps :
#1) Read all the pixel values in the selected window.
#2) Sort the values in ascending order.
#3) Choose the median, that is , the central value.
#4) This value replaces the central pixel of the mask.
#5) Then, move the window by one pixel and repeat the process until the entire image is processed.
#6) Outer rows and columns are not affected by this process.

for k in range(0,3):

	for i in range(0,rows):
		for j in range(0,columns):
		
			#Outer rows and columns are not affected by this process.
			if((i>1)and(i<rows-2)and(j>1)and(j<columns-2)):

				mask_array=[]
		
				#Read all the pixel values in the selected window.
				for m in range(-2,3):

					for n in range(-2,3):

						mask_array.append(img[i+m,j+n,k])

				#Mask of size 5x5
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

				output[i,j,k]=mask_array[12]
    

while(1):

		cv2.imshow('Median Filter Image',output)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

Tkinter.Tk().withdraw() # Close the root window
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,output)
