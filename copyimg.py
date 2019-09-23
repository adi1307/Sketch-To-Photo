# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:12:04 2018

@author: DELL
"""
import cv2

img=cv2.imread("C:\\Users\\DELL\\Desktop\\output\\ney.jpg")
img1=cv2.imread("C:\\Users\\DELL\\Desktop\\proimg\\standard_test_images\\messi.jpg")

for i in range(183):
    for j in range(275):
        color = img[i,j]
        p = all(x!=0 for x in color)
        if p is True:
            img1[i,j]=color

cv2.imshow("messi",img1)
cv2.waitKey(0)

