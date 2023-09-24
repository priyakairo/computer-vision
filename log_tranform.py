import cv2
import numpy as np
img_1= cv2.imread("img/log.jpeg",0)

img_2=np.uint8(np.log1p(img_1))

_,img_3=cv2.threshold(img_2,1,255, cv2.THRESH_BINARY)

cv2.imshow("input image",img_1)
cv2.imshow("log_image",img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
