# import the necessary packages
from labeldetector import LabelDetector
import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import math
import glob
#Rory Spralls
#CSCE 4240
#to build a system that does two parts
# which is a training phase and a operational phase

#training phase
if LabelDetector != 'STOP':
	# Returns a list of names in list files.
	trainfiles = glob.glob(
		'C:\\Users\\rorys\\Documents\\4240 Dig image Processing\\Training\\*', recursive=True) #file pathway
	for file in trainfiles:
		images = cv2.imread(file)


		# load the image and resize it to a smaller factor so that
		# the shapes can be approximated better
		#image = cv2.imread(args["image"])
		resized = imutils.resize(images, width=300)
		ratio = images.shape[0] / float(resized.shape[0])

		# convert the resized image to grayscale, blur it slightly,
		# and threshold it
		gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (5, 5), 0)
		edges = cv2.Canny(blurred, 50, 150)

		w, h = edges.shape[:2]
		#checks if image is inversed or not
		if cv2.countNonZero(gray) > ((w*h)//2):
			thresh = cv2.threshold (edges, 45, 255, cv2.THRESH_BINARY)[1]
			# find contours in the thresholded image and initialize the
			# shape detector
			cnts = cv2.findContours (thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours (cnts)
			ld = LabelDetector ()
		else:
			thresh = cv2.threshold(edges, 240, 255, cv2.THRESH_BINARY)[1]
			# find contours in the thresholded image and initialize the
			# shape detector
			cnts = cv2.findContours (thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours (cnts)
			ld = LabelDetector ()

		# loop over the contours
		for c in cnts:
			# compute the center of the contour, then detect the name of the
			# shape using only the contour
			M = cv2.moments(c)
			if M["m00"] != 0:
				cX = int ((M["m10"] / M["m00"]) * ratio)
				cY = int ((M["m01"] / M["m00"]) * ratio)
			else:
				cX = int (1 * ratio)
				cY = int (1 * ratio)
			shape = ld.detect(c)

			if shape == 'Square':
				Square = images
				#cv2.imshow ("Image", squareIm)
			elif shape == 'Triangle':
				Triangle = images
				#cv2.imshow ("Image", triangleIm)
			elif shape == 'Circle':
				Circle = images
				#cv2.imshow ("Image", circleIm)
			elif shape == 'Ellipse':
				Ellipse = images
				#cv2.imshow ("Image", ellipseIm)
			#elif shape == 'STOP':
				#Unknown = images
				#print('unknown')

			# multiply the contour (x, y)-coordinates by the resize ratio,
			# then draw the contours and the name of the shape on the image
			c = c.astype("float")
			c *= ratio
			c = c.astype("int")
			cv2.drawContours(images, [c], -1, (0, 255, 0), 2)
			cv2.putText(images, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


	# does chord length of images
	arr = np.array(Circle)
	#print(arr)
	#does the 1000 times randomly
	for arr in range(1000):
			bPoint = random.uniform(0, 1) * 360
			ePoint = random.uniform(0, 1) * 360

			r1 = math.cos(bPoint)
			s1 = math.sin(bPoint)
			r2 = math.cos(ePoint)
			s2 = math.sin(ePoint)

			#calculates the chord length
			ChordLength = math.sqrt(math.pow((r1 - r2), 2) + math.pow((s1 - s2), 2))
			#Edistance = math.sqrt(r1*r2 + s1*s2)
			#Edistance = math.sqrt(ChordLength*ChordLength + ChordLength*ChordLength)

	print('Average chord1: ', ChordLength)
	array = np.array(Triangle)
	#print(array)
	for array in range(1000):
			bPoint = random.uniform(0, 1) * 360
			ePoint = random.uniform(0, 1) * 360

			r1 = math.cos(bPoint)
			s1 = math.sin(bPoint)
			r2 = math.cos(ePoint)
			s2 = math.sin(ePoint)

			#calculates the chord length
			ChordLength1 = math.sqrt(math.pow((r1 - r2), 2) + math.pow((s1 - s2), 2))
			#Edistance = math.sqrt(r1*r2 + s1*s2)
			#Edistance = math.sqrt(ChordLength*ChordLength + ChordLength*ChordLength)

	print('Average chord2: ', ChordLength1)
	array1 = np.array(Square)
	#print(array1)
	for array1 in range(1000):
			bPoint = random.uniform(0, 1) * 360
			ePoint = random.uniform(0, 1) * 360

			r1 = math.cos(bPoint)
			s1 = math.sin(bPoint)
			r2 = math.cos(ePoint)
			s2 = math.sin(ePoint)

			#calculates the chord length
			ChordLength2 = math.sqrt(math.pow((r1 - r2), 2) + math.pow((s1 - s2), 2))
			#Edistance = math.sqrt(r1*r2 + s1*s2)
			#Edistance = math.sqrt(ChordLength*ChordLength + ChordLength*ChordLength)

	print('Average chord3: ', ChordLength2)
	array2 = np.array(Ellipse)
	#print(array2)
	for array2 in range(1000):
			bPoint = random.uniform(0, 1) * 360
			ePoint = random.uniform(0, 1) * 360

			r1 = math.cos(bPoint)
			s1 = math.sin(bPoint)
			r2 = math.cos(ePoint)
			s2 = math.sin(ePoint)

			#calculates the chord length
			ChordLength3 = math.sqrt(math.pow((r1 - r2), 2) + math.pow((s1 - s2), 2))
			#Edistance = math.sqrt(r1*r2 + s1*s2)
			#Edistance = math.sqrt(ChordLength*ChordLength + ChordLength*ChordLength)

	print('Average chord4: ', ChordLength3)
	#cv2.imshow('image',images)


#elif LabelDetector != 'STOP':
	#does operational phase
	# Returns a list of names in list files.
	opfiles = glob.glob(
		'C:\\Users\\rorys\\Documents\\4240 Dig image Processing\\Test\\*', recursive=True) #file pathway
	for file in opfiles:
		images = cv2.imread(file)
		cv2.waitKey (0)
		# construct the argument parse and parse the arguments
		

		# load the image and resize it to a smaller factor so that
		# the shapes can be approximated better
		resized = imutils.resize(images, width=300)
		ratio = images.shape[0] / float(resized.shape[0])

		# convert the resized image to grayscale, blur it slightly,
		# and threshold it
		gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (5, 5), 0)
		edges = cv2.Canny(blurred, 50, 150)

		w, h = edges.shape[:2]
		#checks if image is inversed or not
		if cv2.countNonZero(gray) > ((w*h)//2):
			thresh = cv2.threshold (blurred, 1, 255, cv2.THRESH_BINARY_INV)[1]
			if np.all(thresh == 0):
				thresh = cv2.threshold (edges, 60, 255, cv2.THRESH_BINARY)[1]
			# find contours in the thresholded image and initialize the
			# shape detector
			cnts = cv2.findContours (thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours (cnts)
			ld = LabelDetector ()
		else:
			thresh = cv2.threshold(blurred, 1, 255, cv2.THRESH_BINARY)[1]
			# find contours in the thresholded image and initialize the
			# shape detector
			cnts = cv2.findContours (thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours (cnts)
			ld = LabelDetector ()

		# loop over the contours
		for c in cnts:
			# compute the center of the contour, then detect the name of the
			# shape using only the contour
			M = cv2.moments(c)
			if M["m00"] != 0:
				cX = int ((M["m10"] / M["m00"]) * ratio)
				cY = int ((M["m01"] / M["m00"]) * ratio)
			else:
				cX = int (1 * ratio)
				cY = int (1 * ratio)
			shape = ld.detect(c)


			if shape == 'Square':
				showimg = Square
			elif shape == 'Triangle':
				showimg = Triangle
			elif shape == 'Circle':
				showimg = Circle
			elif shape == 'Ellipse':
				showimg = Ellipse
			elif shape == 'STOP':
				print('unknown')

			# multiply the contour (x, y)-coordinates by the resize ratio,
			# then draw the contours and the name of the shape on the image
			c = c.astype("float")
			c *= ratio
			c = c.astype("int")
			cv2.drawContours(images, [c], -1, (0, 255, 0), 2)
			cv2.putText(images, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
			#cv2.imshow ("file", images)
			#cv2.waitKey (0)


			cv2. imshow('training', images)
			cv2.imshow('testing', showimg)
			cv2.waitKey (0)
