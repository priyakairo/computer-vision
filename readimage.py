#read an image from the input and show image on the screen


import cv2
img=cv2.imread("img/self.jpg")
print(type(img))
print(img.shape)
cv2.imshow("window",img)
cv2.waitKey(0)
