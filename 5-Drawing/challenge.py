import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

red, black, green = (0, 0, 255), (0, 0, 0), (0, 255, 0)

for i in range(0, 300, 5):
    for j in range(0, 300, 5):
        if i%10 ==0:
            if j % 10 != 0:
                cv2.rectangle(canvas, (j, i), (j + 5, i + 5), red, -1)
            else:
                cv2.rectangle(canvas, (j, i), (j + 5, i + 5), black, -1)
        else:
            if j % 10 == 0:
                cv2.rectangle(canvas, (j, i), (j + 5, i + 5), red, -1)
            else:
                cv2.rectangle(canvas, (j, i), (j + 5, i + 5), black, -1)
    
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0]//2)
cv2.circle(canvas, (centerX, centerY), 40, green, -1)
cv2.imshow("Square Boxes", canvas)
cv2.waitKey(0)