import cv2

# Load the two images you want to fuse
image1 = cv2.imread("img/self.jpg")
image2 = cv2.imread("img/tree.webp")

# Make sure the two images have the same dimensions
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Specify the weight for each image (alpha and beta values)
alpha = 0.7  # Weight for image1
beta = 0.3   # Weight for image2

# Blend the two images
blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0.0)

# Display the blended image
cv2.imshow("Blended Image", blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
