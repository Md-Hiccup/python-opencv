import numpy as np 
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("Original", image)

#   [1, 0, tx]  tx: no. of pixels to shift the image left or right
#   [1, 0, tx]  tx: -tx => shift Left and +tx => shift Right
#   [0, 1, ty]  ty: no. of pixels to shift the image up or down
#   [0, 1, ty]  ty: -ty => shift up and +ty => shift down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])      
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
# cv2.waitKey(0)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("shifted Down", shifted)
cv2.waitKey(0)