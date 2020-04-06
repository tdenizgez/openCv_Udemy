# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:43:00 2020

@author: tdenizgez
"""


import cv2

img = cv2.imread(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/contour.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,threshold = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)


"""
Moment fonksiyonu dictonary dondurur
Görseldeki nesnenin ağırlık merkezini bulmak için dictoranarydeki değerleri kullanılır:
x--> m10/m00
y--> m01/m00
"""

m = cv2.moments(threshold)
x = int(m["m10"]/m["m00"])
y = int(m["m01"]/m["m00"])

cv2.circle(img, (x,y), 3, (0,0,255),-1)

cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()

