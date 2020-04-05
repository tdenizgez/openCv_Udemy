# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:14:00 2020

@author: tdenizgez
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt


img = np.zeros((500,500),np.uint8) 
cv2.rectangle(img, (50,50), (250,250), (255,255,255),-1)
cv2.imshow("img",img)

"""
ravel() fonksiyonu görüntü matrisi tek bir satıra dökmektedir.
böylece görüntünün hsitoramını çizebiliyoruz.
"""
#plt.hist(img.ravel(),256,[0,256])
#plt.show()


image = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\heli.jpg")
blue = image[:,:,0]
green = image[:,:,1]
red = image[:,:,2]
# r,g,b degerlerini almak icin b,g,r = cv2.split(img) de kullanılabilir
plt.hist(blue.ravel(),256,[0,256])
plt.hist(green.ravel(),256,[0,256])
plt.hist(red.ravel(),256,[0,256])
plt.show


cv2.waitKey()
cv2.destroyAllWindows()