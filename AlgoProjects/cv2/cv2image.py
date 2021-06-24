
import cv2
import numpy as np

path = 'image\jh.jpg'

def changefunction(a):
        pass
    
cv2.namedWindow("colorPicker")
cv2.resizeWindow("colorPicker", 600, 250)
cv2.createTrackbar("teinte min", "colorPicker", 0, 179, changefunction)
cv2.createTrackbar("teinte max", "colorPicker", 179, 179, changefunction)
cv2.createTrackbar("saturation min", "colorPicker", 0, 255, changefunction)
cv2.createTrackbar("staurarion max", "colorPicker", 255, 255, changefunction)
cv2.createTrackbar("valeure min", "colorPicker", 0, 255, changefunction)
cv2.createTrackbar("valeure max", "colorPicker", 255, 255, changefunction)



while True:
	image = cv2.imread(path)
	hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
	t_min = cv2.getTrackbarPos("teinte min", "colorPicker")
	t_max = cv2.getTrackbarPos("teinte max", "colorPicker")
	s_min = cv2.getTrackbarPos("saturation min", "colorPicker")
	s_max = cv2.getTrackbarPos("saturation max", "colorPicker")
	v_min = cv2.getTrackbarPos("valeure min", "colorPicker")
	v_max = cv2.getTrackbarPos("valeure max", "colorPicker")

	min_result = np.array([t_min, s_min, v_min])
	max_result = np.array([t_max, s_max, v_max])
	maskchanged = cv2.inRange(hsvImage, min_result, max_result)
 
	cv2.imshow("normal", image)	
	cv2.imshow("maskcolor", maskchanged)
 
	
	
	
     

