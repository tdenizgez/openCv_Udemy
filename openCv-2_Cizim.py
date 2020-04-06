# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:24:07 2020

@author: tdenizgez
"""


import cv2
import numpy as np

imgCizgi = np.zeros((512,512,3),np.uint8) #0lardan olusan matris olustur.
                                     #Boylece siyah gorsel olusturduk
cv2.line(imgCizgi,(0,0),(512,512),(255,255,255)) #image,baslangic Nok,bitis Nok, Renk, Kalinlik...

imgDortgen =np.zeros((512,512,3),np.uint8)
cv2.rectangle(imgDortgen, (40,40), (120,120), (255,255,255)) # dorgenin iki kosegen noktasinin koordinatlarini girdik

imgDaire =np.zeros((512,512,3),np.uint8)
cv2.circle(imgDaire, (256,256),50, (255,255,255))#Merkez nokta,yaricap,renk,kalinlik...


cv2.imshow("imageCizgi",imgCizgi)
cv2.imshow("imageDortgen",imgDortgen)
cv2.imshow("imageDaire",imgDaire)
cv2.waitKey()
cv2.destroyAllWindows()