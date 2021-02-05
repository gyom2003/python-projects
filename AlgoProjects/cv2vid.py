import cv2
import numpy as np


face_reference = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

videocapture = cv2.VideoCapture(0),


while True:
    img = cv2.VideoCapture(0).read()

    cvtColor = cv2.UMat(img)# cv2.UMat(img), np.float32()

    gray = cv2.cvtColor(cvtColor, cv2.COLOR_BGR2GRAY)

    faces_detection = face_reference.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces_detection:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    frames = cv2.waitKey(1) & 0xff == ord('q')
    if frames == 27:
        break

videocapture.realeased()
cv2.destroyAllWindows()

#a corriger et à améliorer
