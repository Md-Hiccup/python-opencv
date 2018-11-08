"""
While working with images, we need to keep in mind the limits of our color spaces and data types.
Ex: RGB have [0, 255], 
    we examine a pixel with intensity 250 and try to add 10. 
    it will give error b'cuz 260 is not a valid value.

Keep in mind that there is difference b/w OpenCV and NumPy addition
-   Numpy will perform modulo arithmetic and "wrap around".
-   OpenCV will perform clipping and ensure pixel values never fall outside the range [0, 255]

If you want all values to be clipped if they fall outside [0-255] then, use OpenCV's
If you want modulus arithmetic operations and have values wrap around if they fall outside the range [0-255], use NumPy
"""

from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))   #   255
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100])))) #   0

print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))  #   44  
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))   #   206

M = np.ones(image.shape, dtype="uint8") * 100       #   Multiply matrix of 1 by 100
#   It increase every pixel intensity in the image by 100, if value > 255 , it clipped to 255
added = cv2.add(image, M)       
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype="uint8") * 50  #   Multiply matrix of 1 by 50
#   It decrease every pixel intensity in the image by 50, if value < 0 , it clipped to 0
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)