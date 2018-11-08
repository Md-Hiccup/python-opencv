import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

#   Remember OpenCV represent images as Numpy arrays.
#   Numpy represent Images as [ Height First , Width Second ]
#   it means we supply our y-axis value before our x-axis
#   Rectangular region starting at (240, 30) and ending at (335, 120)

#   cropped = image[ y1:y2, x1:x2]

# cropped = image[30:120, 240:335]
cropped = image[35:125, 160:267]

cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)