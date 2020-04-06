# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:11:18 2020

@author: tdenizgez
"""


import cv2
import numpy as np


contour = cv2.imread(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/contour.png")
text = cv2.imread(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/text.png")

gray_contour = cv2.cvtColor(contour, cv2.COLOR_BGR2GRAY)
gray_text = cv2.cvtColor(text, cv2.COLOR_BGR2GRAY)


"""
Oncelikle goodFeaturesToTrack fonsiyonunda kullanabilmek için diziyi float yapmamız gerekmekte
Float yapılmış diziyi fonksiyona sokuyoruz
1.Parametre--> Görsel
2.Parametre--> Max Köşe Sayısı
3.Parametre--> qualityLevel -->0.01 ver
4.Parametre--> Minumum Mesafe oranı
"""
gray_text = np.float32(gray_text)
corners_text = cv2.goodFeaturesToTrack(gray_text, 50, 0.01,10)
corners_text = np.int0(corners_text)

for corner in corners_text:
    x,y = corner.ravel()
    cv2.circle(text, (x,y), 3, (0,0,255),-1)


cv2.imshow("corners_text",text)


gray_contour = np.float32(gray_contour)
corners_contour = cv2.goodFeaturesToTrack(gray_contour, 3, 0.01,10)
corners_contour = np.int0(corners_contour)

for corner in corners_contour:
    x,y = corner.ravel()
    cv2.circle(contour, (x,y), 3, (0,0,255))

cv2.imshow("corner_contours",contour)






cv2.waitKey()
cv2.destroyAllWindows()