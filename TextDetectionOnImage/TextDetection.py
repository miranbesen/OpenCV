# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:21:43 2021

@author: miran
"""

# import cv2 as cv
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd =r'C:\\Program Files\\Tesseract-OCR\tessdata\\tesseract.exe'

# img=cv.imread('2.png')
# # img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))
# cv.imshow('Result',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

import pytesseract

import cv2 as cv

import matplotlib.pyplot as plt  

pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
 
img=cv.imread('2.png')

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

# plt.imshow(img)

hImg, wImg,_=img.shape

boxes =pytesseract.image_to_data(img)

# print(boxes)


for x,b in enumerate(boxes.splitlines()):
    # print(b)
    if x!=0:
        b=b.split()
        print(b)
        if len(b)==12:
            x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv.rectangle(img,(x,y), (w+x,h+y),(0,0,255),3)
            cv.putText(img,b[11],(x,y),cv.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
    
cv.imshow('Result',img)
cv.waitKey(0)
cv.destroyAllWindows()