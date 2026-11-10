import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# Daniel Gallegos NC 1392
print("Daniel Gallegos NC 1392")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
Mi_imagen = cv2.imread('CiudadByN.jpeg')
plt.imshow(Mi_imagen)
plt.title('Ciudad ByN y Daniel Gallegos 1392')
plt.show()

print("+-+-+- Puntos en la imagen -+-+-+")
plt.imshow(Mi_imagen)
x = [100,100,300,269]
y = [ 100,400,500,385]
plt.scatter(x,y, s=20,c='red')
plt.show()