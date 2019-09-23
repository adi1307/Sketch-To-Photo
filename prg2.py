# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:20:16 2018

@author: DELL
"""
import numpy as np
import cv2


img = cv2.imread("/Users/sarthakdandriyal/Desktop/ny.jpeg")
#img = cv2.imread("C:\\Users\\DELL\\Desktop\\proimg\\standard_test_images\\messi.jpg")

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (0,0,250,250)
#rect =(50,50,200,200)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imshow("Image", img)
cv2.waitKey(0)

#plt.imshow(img)
#plt.colorbar()
#plt.show()
