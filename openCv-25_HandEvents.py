# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:38:16 2020

@author: tdenizgez
"""


import cv2
import numpy as np

def nothing(x):
    pass


def findMaxContours(contours):
    maxI = 0
    maxA = 0
    
    for i in range(len(contours)):
        if maxA < cv2.contourArea(contours[i]):
            maxA = cv2.contourArea(contours[i])
            maxI  = i
            
    return contours[maxI]

cap = cv2.VideoCapture(0)


while True:
    _,frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    roi = frame[:,320:]
    
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower = np.array([0,70,90],dtype=np.uint8)
    upper = np.array([180,109,132],dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)
    
    kernel = np.ones((5,5))
    mask = cv2.dilate(mask, kernel,3)
    
    mask = cv2.GaussianBlur(mask, (3,3), 8)
    
    contours,_=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    c = findMaxContours(contours)
    
    cv2.drawContours(roi, c, -1, (0,0,255))
    
    cv2.imshow("mask",mask)
    cv2.imshow("roi",roi)
    
    
    if cv2.waitKey(3) & 0xFF == ord('q'):
       break
    
    
    

cap.release()
cv2.waitKey()
cv2.destroyAllWindows()