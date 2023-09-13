import imaplib
import cv2
import numpy as np
img=cv2.imread("img/self.jpg")
img1=img[:,:,0]
img2=img[:,:,1]
img3=img[:,:,2]

newimg=np.hstack((img1,img2,img3))
cv2.imshow("window",newimg)
cv2.waitKey(0)