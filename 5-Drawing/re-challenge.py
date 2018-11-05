import numpy as np 
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

for row, k in enumerate(range(0, 300, 10)):
    for col, v in enumerate(range(0, 300, 10)):
        color = (0, 0, 255)

        if row%2 == col%2:
            color = (0, 0, 0)

        cv2.rectangle(canvas, (k, v), (k + 10, v + 10), color, -1)
        
cv2.circle(canvas, (150, 150), 50, (0, 255, 0), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)