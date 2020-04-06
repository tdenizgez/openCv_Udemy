# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:46:36 2020

@author: tdenizgez
"""

import cv2
import numpy as np


img = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\helikopter.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)

cv2.imshow("Frame",img)
cv2.imshow("MASK",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()