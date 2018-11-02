import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

red, green = (0, 0, 255), (0, 255, 0)


# for i in range(0, 300, 10):
#     if i % 5 == 0:
#         cv2.rectangle(canvas, (i, i), (i+10, i+10), red, -1)
    
cv2.imshow("Square Boxes", canvas)
cv2.waitKey(0)