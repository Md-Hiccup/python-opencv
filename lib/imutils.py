import numpy as np
import cv2

def translate(image, x, y):
    """
        [1, 0, tx]  tx: no. of pixels to shift the image left or right
        [1, 0, tx]  tx: -tx => shift Left and +tx => shift Right
        [0, 1, ty]  ty: no. of pixels to shift the image up or down
        [0, 1, ty]  ty: -ty => shift up and +ty => shift down
    """
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    """
        scale 1.0 = same size of an image.
        scale 2.0 = double the size of an image.
        scale 0.5 = halves the size of an image.
    """
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated