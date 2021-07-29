# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:57:35 2021

@author: asus
"""

import cv2 as cv


face_cascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml") #classifier yolunu verdik. 

foto=cv.imread("photos/1.jpg")


gray=cv.cvtColor(foto, cv.COLOR_BGR2RGB) #renk ayarlarını tutacak degiskenimizi ayarlıyoruz.

faces= face_cascade.detectMultiScale(gray,1.3,4)

# print(faces)

for(x,y,w,h) in faces: #veritabanımız içinde forla donup kontrol ediyoruz. 
    cv.rectangle(foto,(x,y) , (x+w,y+h),(0,250,0),8)


cv.namedWindow("foto",cv.WINDOW_NORMAL)

cv.imshow("foto",foto)

cv.waitKey(0)

cv.destroyAllWindows()






