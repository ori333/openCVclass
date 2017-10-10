import numpy as np
import cv2  #add OpenCV Library

cap = cv2.VideoCapture(0)

while(True):
	# capture frame by frame
	ret, frame = cap.read()

	cv2.imshow('frame', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destrotyAllWindows()


