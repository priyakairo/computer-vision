import cv2
import numpy as np

img= cv2.imread("img/self.jpg",0)

ret,th1=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

cv2.imshow("window1",img)
cv2.imshow("window",th1)
cv2.waitKey(0)