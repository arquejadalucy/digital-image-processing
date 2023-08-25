import cv2
import numpy as np

# lê uma imagem
img = cv2.imread('imagem 5.jpg')


# converte em nível de cinza
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('rgb',img)

cv2.imshow('hsv',hsv)
