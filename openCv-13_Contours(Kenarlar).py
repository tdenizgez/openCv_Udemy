# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:19:36 2020

@author: tdenizgez
"""


import cv2

image = cv2.imread(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/kenarlar.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

contours,_= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

"""
DrawContours
1. Parametre --> image
2. Parametre --> kenar koordinatları
3. Parametre --> Nerelerin çizileceği
4. Parametre --> Renk
5. Parametre --> Kalınlık
"""
img = cv2.drawContours(image, contours, -1,(0,0,255),3) 

cv2.imshow("contours",img)
cv2.waitKey()
cv2.destroyAllWindows()