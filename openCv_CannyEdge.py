# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:54:17 2020

@author: tdenizgez
"""


import cv2
import numpy as np

"""

Canny fonksiyonu parametre olarak görüntü,minThreshold,maxThreshold almakta
burada manuel threhold yapılmış
threshhold üzerinde smoothing yapılmış
ve orijinal image üzerinde kenar tespiti yapılmıştır

"""


img = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\heli.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th1 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
th1_smooth = cv2.medianBlur(th1, 3)


edges = cv2.Canny(img,100,200)
edges_thresholded = cv2.Canny(th1, 100,200)
edges_smoothed_thresholded = cv2.Canny(th1_smooth, 100,200)

cv2.imshow("orijinal_image",edges)
cv2.imshow("edges_thresholded",edges_thresholded)
cv2.imshow("edges_smoothed_thresholded",edges_smoothed_thresholded)



cv2.waitKey()
cv2.destroyAllWindows()