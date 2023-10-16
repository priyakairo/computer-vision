import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('img/fracture.jpeg', cv2.IMREAD_COLOR)

# Check if the image is loaded properly
if image is None:
    print('Error: Could not open or find the image.')
    exit()

# Convert the image to grayscale (if it's not already)
if len(image.shape) == 3 and image.shape[2] == 3:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    gray_image = image

# Calculate the histogram
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Convert the histogram to a 1D array
hist = hist.ravel()

# Create an array for pixel values (0 to 255)
pixel_values = np.arange(256)

# Plot the histogram
plt.bar(pixel_values, hist, width=1.0, color='b')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram of Image')
plt.grid(True)

# Show the histogram
plt.show()


#output----



