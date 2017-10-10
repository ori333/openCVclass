# import the necessary packages
import cv2
import numpy as np
imgColor = cv2.imread('shapes_and_colors.png',1) # 0

class ShapeDetector:
	def __init__(self):
		pass
 
	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
		# if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "triangle"
 
		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
 
			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
 
		# if the shape is a pentagon, it will have 5 vertices
		elif len(approx) == 5:
			shape = "pentagon"
 
		# otherwise, we assume the shape is a circle
		else:
			shape = "circle"
 
		# return the name of the shape
		return shape

#Find contour
imgray = cv2.cvtColor(imgColor,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,75,255,0)
cv2.waitKey(0)

cv2.imshow('threshold',thresh)
cv2.waitKey(0)



#find the iris contour
#4 for this image
_, contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
sd = ShapeDetector()
for contour in contours:
	if cv2.contourArea(contour) > 1000 and cv2.contourArea(contour) < 20000: 
		cv2.drawContours(imgColor, contour, -1, (0,255,0), 3)
		shape = sd.detect(contour)
		print shape

		#Find center of the shape
		# shape using only the contour
		M = cv2.moments(contour)
		cX = int((M["m10"] / M["m00"]) )
		cY = int((M["m01"] / M["m00"]) )
		cv2.putText(imgColor, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (255, 255, 255), 2)



cv2.imshow("Contours",imgColor)
cv2.waitKey(0)
