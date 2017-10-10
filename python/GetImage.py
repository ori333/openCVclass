import numpy as np
import cv2  #add OpenCV Library

img = cv2.imread('image.jpg',1) # 0

print img.shape #BGR

#img[:,:,0] = 0 

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()