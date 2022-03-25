import cv2 as cv
import sys

# import des bibliothèques nécessaires à l'exécustion du code OpenCV

img = cv.imread("First_night.jpg")

# Lecture de l'image par OpenCV


# Affichage de l'image 

from  matplotlib import pyplot as plt 

plt.figure(figsize=(5,5))
plt.imshow(img)
plt.show()
