#Imports
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
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
#Reescalamos la imagen
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

#Hacemos la imagen en gris para que sea mas sencillo detectar los colores
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

#Encontramos los contornos y empezamos la deteccion de formas
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetector()

# Hacemos el ciclo para detectar los contornos
for c in cnts:
	# Calculamos el contorno y lo dibujamos
	M = cv2.moments(c)
	if(M["m10"] > 0 and M["m00"] > 0 and M["m01"] > 0):
		cX = int((float(M["m10"]) / float(M["m00"])) * ratio)
		cY = int((M["m01"] / M["m00"]) * ratio)
		shape = sd.detect(c)

		c = c.astype("float")
		c *= ratio
		c = c.astype("int")
		cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
		cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (255, 255, 255), 2)

	# Mostramos la imagen
	cv2.imshow("Image", image)
	cv2.waitKey(0)
