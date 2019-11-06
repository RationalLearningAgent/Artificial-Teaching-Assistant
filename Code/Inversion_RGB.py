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

#Zero Memory point operations

#1) Inversion/Digital Negative

shape_tuple=img.shape
rows=shape_tuple[0]
columns=shape_tuple[1]

output=np.zeros((rows,columns,3),np.uint8)

for k in range(0,3):
	for i in range(0,rows):
		for j in range(0,columns):
		
			output[i,j,k]=256-1-img[i,j,k]

while(1):

		cv2.imshow('Inversion/Digital Negative',output)

		c = cv2.waitKey(1)
	
		if c == 27:
			cv2.destroyAllWindows()
			break

Tkinter.Tk().withdraw() # Close the root window
out_path = tkFileDialog.asksaveasfilename()

cv2.imwrite(out_path,output)
