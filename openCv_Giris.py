# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:50:08 2020

@author: tdenizgez
"""


import cv2
img=cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\helikopter.jpg")
cv2.imshow("helikopter",img)

dugme = cv2.waitKey(0)
"""
iki resmi belli seffalık oranlarında ekleme 

img2 = cv2.imread("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\heli.jpg")
img3 = img2[0:412,0:640]
dst = cv2.addWeighted(img,0.25,img3,0.75,0) ilk resim,ilk resmin orani,ikinci resmin, ikinci resmin orani
cv2.waitKey()
cv2.imshow("dst",dst)
"""
if dugme == 27:
    cv2.destroyAllWindows()
else:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\gri_helikopter.jpg",img_gray)


vid = cv2.VideoCapture("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\lights.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
cikti = cv2.VideoWrite("C:\\Users\\tdenizgez\\Desktop\\OpenCv\\Dosyalar\\sokak.mp4",fourcc,20.0,(640,480))
while(True):
    deger,kare = vid.read()
    cikti.write(kare)
    cv2.imshow("video",kare)
    
    if cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.destroyAllWindows()
        break
    
vid.release()
cv2.destroyAllWindows()