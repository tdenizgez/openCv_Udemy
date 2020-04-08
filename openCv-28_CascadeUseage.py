# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:55:50 2020

@author: tdenizgez
"""


import cv2   

img = cv2.imread(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/sampleFace.png")
face_cascade = cv2.CascadeClassifier(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/face.xml")
eye_cascade = cv2.CascadeClassifier(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
faces = face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow('image',img)

img2 = img[y:y+h, x:x+w]
gray2 = gray[y:y+h, x:x+w]

eyes = eye_cascade.detectMultiScale(gray2)

for (ex,ey,ew,eh) in eyes:
	cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    
img[y:y+h, x:x+w] = img2
         
cv2.imshow('image2',img)

cv2.waitKey(0)
cv2.destroyAllWindows()