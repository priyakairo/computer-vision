#convert the color image into GRAY IMAGE

import cv2

img=cv2.imread("img/self.jpg")

grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("window",grey)
cv2.waitKey(0)
