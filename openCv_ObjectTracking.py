# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:27:09 2020

@author: tdenizgez
"""


import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/dog.mp4")

while True:
    _,frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sensivity = 15
    lower_white = np.array([0,0,255-sensivity])
    upper_white = np.array([255,sensivity,255])
    
    mask = cv2.inRange(hsv,lower_white,upper_white) # aralıkta olan degerleri beyaz olmayanları siyah yapıyor (?)
    res = cv2.bitwise_and(frame, frame,mask=mask) # orijinal görsele maske ekleniyor böylece sadece beyaz olan yerler ayırt edilmiş olabiliyor.
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)
    
    k = cv2.waitKey(5) & 0xFF
    if k== 26:
        break

cv2.destroyAllWindows()