import cv2
import numpy as np

# Load the image
image = cv2.imread('img/self.jpg')

# Define the zoom factor (e.g., 2 for doubling the size)
zoom_factor = 5

# Get the dimensions of the original image
height, width, channels = image.shape

# Create a new blank image with the zoomed dimensions
new_height = int(height * zoom_factor)
new_width = int(width * zoom_factor)
zoomed_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

# Zoom the image by multiplying pixel values
for y in range(new_height):
    for x in range(new_width):
        original_x = int(x / zoom_factor)
        original_y = int(y / zoom_factor)
        zoomed_image[y, x] = image[original_y, original_x]

# Save or display the zoomed image
cv2.imwrite('zoomed_image.jpg', zoomed_image)
cv2.imshow('Zoomed Image', zoomed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
