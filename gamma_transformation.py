import cv2
import numpy as np

img_1= cv2.imread("img/fracture.jpeg",0)

gamma=2
img_2= np.power(img_1, gamma)
cv2.imshow("input",img_1)
cv2.imshow("gaama2",img_2)
cv2.waitKey(0)