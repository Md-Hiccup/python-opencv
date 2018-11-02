from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# cv2.waitKey(0)

#*  Checking the bgr color
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) = Red: {}, Green: {}, Blue: {}".format(r, g, b))

#*  Checking the 
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) = Red: {}, Green: {}, Blue: {}".format(r, g, b))

#* Cropping the image
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

#* Updating the cropping image to color Green
image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)