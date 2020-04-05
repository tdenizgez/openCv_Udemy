# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:23:47 2020

@author: tdenizgez
"""


import cv2
import numpy as np

bitwise_1 = np.zeros((400,800),np.uint8) #y,x 
bitwise_1[:,400:] = 255
cv2.imshow("image",bitwise_1)

bitwise_2 = np.zeros((400,800),np.uint8)
bitwise_2[:,:400] = 255
p1 = (550,200)
p2 = (650,200)
p3 = (600,100)


"""
cv2.line(bitwise_2, p1, p2, (255,255,255))
cv2.line(bitwise_2, p2, p3, (255,255,255))
cv2.line(bitwise_2, p1, p3, (255,255,255))
"""

#İçi Doldurulmus Ucgen Cizmek İcin Çember Çizip Merkezilerini Birleştiriyoruz 
cv2.circle(bitwise_2, p1, 2, (255,255,255), -1)
cv2.circle(bitwise_2, p2, 2, (255,255,255), -1)
cv2.circle(bitwise_2, p3, 2, (255,255,255), -1)
triangle_cnt = np.array( [p1, p2, p3] )
cv2.drawContours(bitwise_2, [triangle_cnt], 0, (255,255,255), -1)
cv2.imshow("image3",bitwise_2)




#Bitwise İslemler

bit_and = cv2.bitwise_and(bitwise_1, bitwise_2)
cv2.imshow("bitwise_and",bit_and)

bit_or = cv2.bitwise_or(bitwise_1, bitwise_2)
cv2.imshow("bitwise_or",bit_or)

bit_xor = cv2.bitwise_xor(bitwise_1, bitwise_2)
cv2.imshow("bitwise_xor",bit_xor)

cv2.waitKey()
cv2.destroyAllWindows()
