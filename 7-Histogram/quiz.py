"""
1. Compute a grayscale histogram for this image. Approximately what bin number has the the highest pixel count?
2. Compute a 2D color histogram for the Red and Green channels of the wave image using 8 bins for each channel. Which bin has the largest pixel count?
"""
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#?  1.  #
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", gray_image)
cv2.waitKey(0)
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

#?  2.  #
chans = cv2.split(image)
print()
colors = ("b", "g", "r")

fig = plt.figure()
ax = fig.add_subplot(111)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [8, 8], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D color histogram for R and G")
plt.colorbar(p)
plt.show()

eq = cv2.equalizeHist(gray_image)
cv2.imshow("Histogram Equalization", np.hstack([gray_image, eq]))
cv2.waitKey(0)
