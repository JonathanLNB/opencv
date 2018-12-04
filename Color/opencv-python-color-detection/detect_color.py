# Imports
import numpy as np
import argparse
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
#Mostramos la camara y esperamos a que teclee q para tomar la imagen
while(True):
        ret, img = cap.read()
        cv2.imshow('TITULO DE VENTANA',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cv2.imwrite("/home/pi/Downloads/Color/opencv-python-color-detection/img.jpg",img)
impath =  "/home/pi/Downloads/Color/opencv-python-color-detection/img.jpg"
#Importamos la imagen
image = cv2.imread(impath)
# Definimos los bordes de deteccion del color
boundaries = [
	([17, 15, 100], [50, 56, 200]), #Rojo
	([86, 31, 4], [220, 88, 50]),   #Azul
	([25, 106, 130], [62, 174, 250]), #Amarillo
	([106, 130, 25], [174, 250, 62]) #Verde
]

# Revisamos todos los bordes de colores
for (lower, upper) in boundaries:
	# Sacamos los bordes como valores escalares
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	#Encontramos lo colores con sus respectivos bordes
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)

	#Mostramos la imagen
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
