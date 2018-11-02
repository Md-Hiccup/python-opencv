from __future__ import print_function   #   for future updating python version 
import argparse     #   to handle parsing our command line arguments
import cv2          #   to import OpenCV library

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])  #   cv2.imread returns a NumPy array representing the image
print("width: {} pixels".format(image.shape[1]))        #   using shape to examine width
print("height: {} pixels".format(image.shape[0]))       #   using shape to examine height
print("channels: {}".format(image.shape[2]))             #   using shape to examine no. of channels

cv2.imshow("Image", image)      #   ( "name of our window", <reference to the image we load line(9)> )
cv2.waitKey(0)  #   pause the execution of the script until we press any key  
cv2.imwrite("newimage.png", image)  #   write image to file in .jpg format


""" Extra Things
print(image.shape)  # (942['height or row'], 942['width or cols'], 3)
"""