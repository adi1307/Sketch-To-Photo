#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:59:24 2018

@author: sarthakdandriyal
"""

import cv2;
import numpy as np;
 
# Read image
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
# Display images.
#cv2.imshow("Thresholded Image", im_th)
#cv2.imshow("Floodfilled Image", im_floodfill)
#img=cv2.imread('sketch.jpg',-1)
cv2.imwrite(p2,im_floodfill)
#cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
#cv2.imshow("Foreground", im_out)
cv2.waitKey(0)
