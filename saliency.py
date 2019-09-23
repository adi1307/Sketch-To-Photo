# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:03:14 2018

@author: DELL
"""
# import the necessary packages
import cv2
 
# construct the argument parser and parse the arguments

 
# load the input image
image = cv2.imread("C:\\Users\\DELL\\Desktop\\proimg\\standard_test_images\\neymar.jpg")
# initialize OpenCV's static saliency spectral residual detector and
# compute the saliency map
saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
(success, saliencyMap) = saliency.computeSaliency(image)
saliencyMap = (saliencyMap * 255).astype("uint8")
cv2.imshow("Image", image)
cv2.imshow("Output", saliencyMap)
cv2.waitKey(0)
# initialize OpenCV's static fine grained saliency detector and
# compute the saliency map
saliency = cv2.saliency.StaticSaliencyFineGrained_create()
(success, saliencyMap) = saliency.computeSaliency(image)
 
# if we would like a *binary* map that we could process for contours,
# compute convex hull's, extract bounding boxes, etc., we can
# additionally threshold the saliency map
threshMap = cv2.threshold(saliencyMap, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# show the images
cv2.imshow("Image", image)
cv2.imshow("Output", saliencyMap)
cv2.imshow("Thresh", threshMap)
cv2.waitKey(0)