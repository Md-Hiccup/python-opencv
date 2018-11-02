import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

#*  to Read and Show an Image
image = mpimg.imread("newimage.png")        #   to load an image as multi-dimensional NumPy array
plt.imshow(image)       #   to Display our image to our screen
plt.show()  #   To show     

#*  to remove axis and then Display an Image
plt.axis("off")         #   to remove numbered axis from the image
plt.imshow(image)
plt.show()

#*   to Display an image using opencv
import cv2

image = cv2.imread("newimage.png")
plt.axis("off")
plt.imshow(image)
plt.show()

#*  opencv represent RGB images as multidimensional Numpy array.. **but in reverse order!**
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()



