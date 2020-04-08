# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:35:49 2020

@author: tdenizgez
"""


import cv2
import numpy as np 
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = cv2.imread(r"C:/Users/tdenizgez/Desktop/OpenCv/Dosyalar/plate.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur_gaus = cv2.GaussianBlur(gray, (5,5),15)
canny = cv2.Canny(blur_gaus, 70, 250)

contours= cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts = contours[0]
cnts = sorted(cnts,key = cv2.contourArea,reverse = True)

screen = None

for c in cnts:
    epsilon = 0.018*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 4:
        screen = approx
        break

xmin = np.min(screen[:,:,0])
ymin = np.min(screen[:,:,1])
xmax = np.max(screen[:,:,0])
ymax = np.max(screen[:,:,1])
plate = image[ymin:ymax,xmin:xmax]

text = pytesseract.image_to_string(plate,lang = "eng")
print("",text)
cv2.imshow("Plate",plate)

cv2.waitKey()
cv2.destroyAllWindows()