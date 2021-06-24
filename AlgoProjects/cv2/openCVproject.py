import cv2
import numpy as np
import random

handpath = 'image\cv2hand.jpg'
micropath = 'image\cv2micro.jpg' #
imagepath = 'image\cv2origin.jpg'
hand = cv2.imread(handpath, cv2.IMREAD_GRAYSCALE)
micro = cv2.imread(micropath, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)

width, height = micropath.shape
templatemethodes = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED,
                    cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
                    cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in templatemethodes:
    imagecopy = cv2.image.copy()
    match = cv2.matchTemplate(imagecopy, micropath)
    


