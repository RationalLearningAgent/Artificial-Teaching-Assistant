from subprocess import call

choice=0

while(choice!=5):

	print "\n*****Main Menu*****"
	print "1. Zero Memory Point Operations"
	print "2. Histogram Processing"
	print "3. Neighbourhood Processing"
	print "4. Edge Detection"
	print "5. Exit"

	choice=input("Enter your choice ")

	if(choice==1):

		choice1=0

		while(choice1!=3):
		

			print "\n*****Zero Memory Point Operations*****"
			print "1. Grayscale Image"
			print "2. RGB Colour Image"
			print "3. Exit"

			choice1=input("Enter your choice ")

			if(choice1==1):

				choice1a=0

				while(choice1a!=6):


					print "\n*****Grayscale Zero Memory Point Operations*****"
					print "1. Inversion / Digital Negative"
					print "2. Threholding"
					print "3. Intensity Level Slicing without Background"
					print "4. Intensity Level Slicing with Background"
					print "5. Bit Plane Slicing"
					print "6. Exit"

					choice1a=input("Enter your choice ")

					if(choice1a==1):

						call(["python","Inversion_Grayscale.py"])	

					elif(choice1a==2):

						call(["python","Thresholding.py"])

					elif(choice1a==3):

						call(["python","Intensity_Level_Slicing_Without_Background.py"])

					elif(choice1a==4):

						call(["python","Intensity_Level_Slicing_With_Background.py"])
			
					elif(choice1a==5):

						call(["python","Bit_Plane_Slicing.py"])

					elif(choice1a==6):

						print "Exiting\n"

					else:

						print "Invalid Choice\n"

	

	
			elif(choice1==2):

				choice1b=0

				while(choice1b!=3):

		
					print "\n*****RGB Colour Image Zero Memory Point Operations*****"
					print "1. Inversion / Digital Negative"
					print "2. Image Text Colour"
					print "3. Exit"

					choice1b=input("Enter your choice ")

		
					if(choice1b==1):

						call(["python","Inversion_RGB.py"])
		
					elif(choice1b==2):

						call(["python","RGB_Text_Colour.py"])

					elif(choice1b==3):
		
						print "Exiting\n"

					else:

						print "Invalid Choice\n"






			elif(choice1==3):

				print "Exiting\n"

		
		
			else:
	
				print "Invalid Choice\n"
				
	





	elif(choice==2):

		choice2=0

		while(choice2!=4):

			print "\n*****Histogram Processing*****"
			print "1. Grayscale Image Histogram Equalization"
			print "2. RGB Colour Image Histogram Equalization Method 1"
			print "3. RGB Colour Image Histogram Equalization Method 2"
			print "4. Exit"

			choice2=input("Enter your choice ")



			if(choice2==1):

				call(["python","Histogram_Equalization_Grayscale_Short.py"])

			elif(choice2==2):

				call(["python","Histogram_Equalization_RGB_Method_1_Short.py"])

			elif(choice2==3):

				call(["python","Histogram_Equalization_RGB_Method_2_Short.py"])

			elif(choice2==4):

				print "Exiting\n"

			else:

				print "Invalid Choice\n"
			









	elif(choice==3):

		choice3=0

		while(choice3!=3):


		
			print "\n*****Neighbourhood Processing Operations*****"
			print "1. Grayscale Image"
			print "2. RGB Colour Image"
			print "3. Exit"

			choice3=input("Enter your choice ")

		
	
			if(choice3==1):

				choice3a=0

				while(choice3a!=7):


					print "\n*****Grayscale Neighbourhood Processing Operations*****"
					print "1. Image Smoothing 3x3"
					print "2. Image Smoothing 5x5"
					print "3. Image Sharpening (No Diagonal Elements)"
					print "4. Image Sharpening (Diagonal Elements)"
					print "5. Noise Removal (Median Filter 3x3)"
					print "6. Noise Removal (Median Filter 5x5)"
					print "7. Exit\n"

					choice3a=input("Enter your choice ")

					if(choice3a==1):

						call(["python","Image_Smoothing_3x3.py"])

					elif(choice3a==2):

						call(["python","Image_Smoothing_5x5.py"])

					elif(choice3a==3):

						call(["python","No_Diagonal_Elements.py"])

					elif(choice3a==4):

						call(["python","Diagonal_Elements.py"])

					elif(choice3a==5):

						call(["python","Median_Filter_3x3.py"])

					elif(choice3a==6):

						call(["python","Median_Filter_5x5.py"])

					elif(choice3a==7):

						print "Exiting\n"

					else:

						print "Invalid Choice\n"





			elif(choice3==2):

				choice3b=0

				while(choice3b!=7):

			
					print "\n*****RGB Colour Image Neighbourhood Processing Operations*****"
					print "1. Image Smoothing 3x3"
					print "2. Image Smoothing 5x5"
					print "3. Image Sharpening (No Diagonal Elements)"
					print "4. Image Sharpening (Diagonal Elements)"
					print "5. Noise Removal (Median Filter 3x3)"
					print "6. Noise Removal (Median Filter 5x5)"
					print "7. Exit\n"

					choice3b=input("Enter your choice ")

					if(choice3b==1):

						call(["python","Image_Smoothing_RGB_3x3.py"])

					elif(choice3b==2):
			
						call(["python","Image_Smoothing_RGB_5x5.py"])

					elif(choice3b==3):
		
						call(["python","No_Diagonal_Elements_RGB.py"])

					elif(choice3b==4):

						call(["python","Diagonal_Elements_RGB.py"])

					elif(choice3b==5):

						call(["python","Median_Filter_RGB_3x3.py"])

					elif(choice3b==6):

						call(["python","Median_Filter_RGB_5x5.py"])

					elif(choice3b==7):

						print "Exiting\n"

					else:

						print "Invalid Choice\n"


			elif(choice3==3):

					print "Exiting\n"

		
			else:

					print "Invalid Choice\n"












	elif(choice==4):


		choice4=0

		while(choice4!=3):


			print "\n*****Edge Detection*****"
			print "1. Previtt Masks"
			print "2. Sobel Masks"
			print "3. Exit"

			choice4=input("Enter your choice : ")

			if(choice4==1):

				call(["python","Previtt.py"])

			elif(choice4==2):

				call(["python","Sobel.py"])

			elif(choice4==3):

				print "Exiting\n"

			else:
			
				print "Invalid Choice\n"













	elif(choice==5):

		print "\nThanks for using the application.\n"









	else:

		print "Invalid Operation\n"



