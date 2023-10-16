import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('img/self.jpg',cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded properly
if image is None:
    print('Error: Could not open or find the image.')
    exit()

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display the original and equalized images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.show()
