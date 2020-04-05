
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:50:32 2020

@author: tdenizgez
"""


import cv2
import numpy as np

vid = cv2.VideoCapture(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/road.mp4")

while True:
    ret,frame=vid.read()
    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # hsv range for ...
    
    lower_yellow = np.array([18,94,140],np.uint8)
    upper_yellow = np.array([48,255,255],np.uint8)

    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    edges = cv2.Canny(mask,75,250)

    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)

    for line in lines:
        (x1,y1,x2,y2) = line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow("IMG",frame)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

"""

Çizgi Tespiti Yapabiliyor ancak görselin kesilmesi ve kesilen yerlerin karartılması lazım
Bunun için yola kuşbakışı olarak bakılmalı
while True:
    _,frame = vid.read()
    
    x,y,_ = frame.shape
    x= int(x/2)
    frame =  frame[x+150:,400:-400]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #cv2.imshow("img",gray)
    
    edges = cv2.Canny(gray, 200, 300)
    
    cv2.imshow("canny",edges)
    lines = cv2.HoughLinesP(edges, 5, np.pi/180, 50,maxLineGap=200)
    for line in lines:
        x1,y1,x2,y2 =line[0]
        cv2.line(edges, (x1,y1), (x2,y2), (255,255,255))
        cv2.imshow("lines",edges)
    
    
    
     
    if cv2.waitKey(20) &0xFF == ord('q'):
        break


"""

vid.release()
cv2.destroyAllWindows()