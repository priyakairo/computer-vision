import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('img/download.jpeg3333333333333333333333333333', cv2.IMREAD_COLOR)

# Check if the image is loaded properly
if image is None:
    print('Error: Could not open or find the image.')
    exit()

# Split the image into its color channels
blue_channel, green_channel, red_channel = cv2.split(image)

# Calculate the histograms for each color channel
hist_blue = cv2.calcHist([blue_channel], [0], None, [256], [0, 256])
hist_green = cv2.calcHist([green_channel], [0], None, [256], [0, 256])
hist_red = cv2.calcHist([red_channel], [0], None, [256], [0, 256])

# Convert histograms to 1D arrays
hist_blue = hist_blue.ravel()
hist_green = hist_green.ravel()
hist_red = hist_red.ravel()

# Create an array for pixel values (0 to 255)
pixel_values = np.arange(256)

# Plot the histograms
plt.figure(figsize=(8, 6))
plt.plot(pixel_values, hist_blue, color='b', label='Blue')
plt.plot(pixel_values, hist_green, color='g', label='Green')
plt.plot(pixel_values, hist_red, color='r', label='Red')

plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('RGB Histogram of Image')
plt.grid(True)
plt.legend()

# Show the histograms
plt.show()
