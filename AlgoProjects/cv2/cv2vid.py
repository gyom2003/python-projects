import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    ref, frame = cap.read()	
    x, test = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    
    #créer plusieurs instances cam 
    image = np.zeros(frame.shape, np.uint8) 
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_frame
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame
    #cv2.imshow('multiplevideo', image)
    
    #déssiner, ligne autres
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 2) #source, debut, fin, color, thick
    img = cv2.line(img, (0, height), (width, 0), (255, 128, 0), 2)
    img = cv2.rectangle(img, (150, 250), (250, 450), (120, 120, 50), -1)
    img = cv2.rectangle(img, (100, 200), (250, 250), (120, 120, 50), 2)
    img = cv2.circle(img, (350, 350), 75, (0, 0, 150), 2)
    font = cv2.FONT_HERSHEY_DUPLEX
    img = cv2.putText(img, "random texte", (width-200, height - 20), font, 1, (0, 0, 45), 2, cv2.LINE_AA)
    #cv2.imshow('ligne', img)  
    
    hsv = cv2.cvtColor(test, cv2.COLOR_BGR2HSV) #test image row, column, channel
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue_result = cv2.bitwise_and(test, test, mask=mask)
    
    #cv2.imshow("color_blue", blue_result)
    
     

    if cv2.waitKey(1) == ord('q'):
        break

    
cap.release()
cv2.destroyAllWindows()	


#corner detection 

path = 'image\cv2.png'
img = np.array(path)
img = cv2.imread(path)
img = cv2.resize(img, (0, 0), fx=1, fy=1)
grayscale =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rebords = cv2.goodFeaturesToTrack(grayscale, 200, 0.01, 10)
rebords = np.int0(rebords)  
print(rebords)

for rebord in rebords:
    x, y = rebord.ravel() #numpy array à liste cordonnées 
    print(x, y)
    cv2.circle(img, (x, y), 7, (0, 0, 150), 1)
    
for  i in range(len(rebords)):
    for a in range(i + 1, len(rebords)):
        rebord1 = tuple(rebords[i][0])
        rebord2 = tuple(rebords[a][0])
        #[[i, a]] car pas .ravel()
        randomcolor = tuple(map(lambda x : int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, rebord1, rebord2, randomcolor, 1)
        
for t in enumerate(rebords):
    pass
        
cv2.imshow("cornerimage", img)
cv2.waitKey(0)



