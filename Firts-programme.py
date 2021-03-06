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

# Coloriser l'image 

gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Flouter l'image 

blur = cv.GaussianBlur(gris,(11,11),0)

