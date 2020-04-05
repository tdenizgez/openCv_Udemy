# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:21:41 2020

@author: tdenizgez
"""


import cv2
import numpy as np

img = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\helikopter.jpg",0)# 0 Gri okumasını sağladı
row,col = img.shape

"""
 ############# RESMI KAYDIRMA ISLEMI #############
 dizilerin 3. elemanları ne kadar kaydırılacağını belirliyor
 1,0,100-->soldan 100 birim kaydır
 0,1,100-->Yukarıdan 100 birim kaydır

"""
M = np.float32([[1,0,100],[0,1,100]]) 
dst = cv2.warpAffine(img, M, (row,col))
cv2.imshow("KaydırılmısGoruntu",dst)

"""
 ############# RESMI DONDURME ISLEMI #############
 ilk parametre dizinin merkez noktasını alıyor bu yüzden satır sutun sayısının yarısını verdik
 ikinci parametre döndürme oranını istiyor
 ücüncü parametre ise ölçeğini istiyor
 
"""
mat = cv2.getRotationMatrix2D((col/2, row/2),90,1)

dst1 = cv2.warpAffine(img, mat, (row,col))
cv2.imshow("DondurulmusGoruntu",dst1)

"""
 ############# THRESHOLDING #############

Adaptive Thresholding
In the previous section, we used one global value as a threshold. But this might not be good in all cases, e.g. if an image has different lighting conditions in different areas. In that case, adaptive thresholding can help. Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with varying illumination.

In addition to the parameters described above, the method cv.adaptiveThreshold takes three input parameters:

The adaptiveMethod decides how the threshold value is calculated:

cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
The blockSize determines the size of the neighbourhood area and C is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.
"""

image = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\heli.jpg",0)

ret,th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
th3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)


cv2.imshow("threshold-1",th1)
cv2.imshow("threshold-2",th2)
cv2.imshow("threshold-3",th3)




cv2.waitKey(0)
cv2.destroyAllWindows()
