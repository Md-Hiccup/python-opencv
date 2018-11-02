import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")  # 300*300 pixel with 3 channel(RGB), uint8 = unsigned integer 8-bit

#* Drawing Lines
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)  #   ( <draw editor>, <start>, <end>, <color of line>, <thickness>)
cv2.imshow("Canvas 1", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)    #   ( <draw editor>, <start>, <end>, <color of line>, <thickness>)
cv2.imshow("Canvas 2", canvas)
cv2.waitKey(0)

#* Drawing Rectangles
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas 3", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 255), red, 5)
cv2.imshow("Canvas 4", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas 5", canvas)
cv2.waitKey(0)

#* Drawing Circle
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)   # Dividing the Canvas shape (width/2, height/2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas 6", canvas)
cv2.waitKey(0)

#* Abstract Drawing
for i in range(0, 25):
    radius = np.random.randint(5, high=200)     #   radius b/w [5, 200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()  # size = 3 (RGB) 
    pt = np.random.randint(0, high=300, size=(2,))      #   pt [0, 300)
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Abstract Canvas", canvas)
cv2.waitKey(0)