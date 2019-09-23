#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:37:38 2018

@author: sarthakdandriyal
"""

import cv2
import numpy as np
import glob
#downloading images
from google_images_download import google_images_download
s="cat"
response = google_images_download.googleimagesdownload()
arguments = {"keywords":s,"limit":2}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
print(paths) 
# Read image
#hole filling
list=["couple","ik0","ikhf"]
add=[]
path="/Users/sarthakdandriyal/Desktop/"
p1=path+list[0]
p1=p1+".jpg"
im_in = cv2.imread(p1, cv2.IMREAD_GRAYSCALE);
 
# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
 
th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV);
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv
p2=path+list[2]
p2=p2+".jpg" 
cv2.imwrite(p2,im_floodfill)
#crop
#has to be in a loop
img = cv2.imread("lenna.png")
crop_img = img[y:y+h, x:x+w]#coordinates required
cv2.imshow("cropped", crop_img)
#compare
original = cv2.imread("/Users/sarthakdandriyal/Desktop/gubbara.jpg")
# load all the images
sift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = sift.detectAndCompute(original, None)
 
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)
titles=[]
all_images_to_compare=[]
for f in glob.iglob("/Users/sarthakdandriyal/Desktop/baloons/*"):
    image=cv2.imread(f)
    titles.append(f)
    all_images_to_compare.append(image)
for image_to_compare ,title in zip(all_images_to_compare,titles): 
# 1) Check if 2 images are equals
    if original.shape == image_to_compare.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)
     
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Similarity: 100%(equal size and channels)")
    # 2) Check for similarities between the 2 images
    
  
    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)
    
    matches = flann.knnMatch(desc_1, desc_2, k=2)
     
    good_points = []
    for m, n in matches:
        if m.distance < 0.6*n.distance:
            good_points.append(m)
     
    # Define how similar they are
    number_keypoints = 0
    if len(kp_1) <= len(kp_2):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)
     
    print("Title: " + title)
    percentage_similarity=len(good_points) / number_keypoints * 100
    print("Similarity: " + str(int(percentage_similarity)) + "%\n")
 #grabcut
img = cv2.imread("C:\\Users\\DELL\\Desktop\\proimg\\standard_test_images\\messi.jpg")

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#a,b=cv2.imsize(img)

#rect = (10,20,250,250)
rect =(50,50,450,290)#coordinates of image (0,0,b,a)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imshow("Image", img)
cv2.waitKey(0)    
#copy image

img=cv2.imread("C:\\Users\\DELL\\Desktop\\output\\ney.jpg")#image
img1=cv2.imread("C:\\Users\\DELL\\Desktop\\proimg\\standard_test_images\\messi.jpg")#baackground

for i in range(183):
    for j in range(275):
        color = img[i,j]
        p = all(x!=0 for x in color)
        if p is True:
            img1[i,j]=color

cv2.imshow("messi",img1)
cv2.waitKey(0)
