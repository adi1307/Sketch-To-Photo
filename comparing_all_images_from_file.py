#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:33:47 2018

@author: sarthakdandriyal
"""

import cv2
import numpy as np
import glob
path="/Users/sarthakdandriyal/Desktop/"
path=path+"gubbara"
path=path+".jpg"
original = cv2.imread(path)
sim=0.0
pth=""
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
     

    ps=len(good_points) / number_keypoints
    if(ps>sim):
       sim=ps
       pth=title
print(pth)
print(sim)       
     
