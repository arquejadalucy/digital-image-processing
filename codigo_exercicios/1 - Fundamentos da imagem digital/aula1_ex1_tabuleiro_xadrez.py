"""
1) Crie uma imagem 400 x 400 e utilizando o opencv com o python
a transforme num tabuleiro de xadrez aonde cada quadrado seja do tamanho 50x50.
"""
import cv2
import numpy as np

image_height = 100
image_width = 100
number_of_color_channels = 3
black = (0, 0, 0)
white = (255, 255, 255)

# Creating 100x100 black image
img_array = np.full(
    (image_height, image_width, number_of_color_channels),
    black, dtype=np.uint8)
print(img_array.shape)
print(img_array[int(image_width / 2)+3, int(image_height / 2)+3])
# Creating the 50x50 white squares to obtain the chess board
img_array[int(image_width / 2):image_width,
          int(image_height / 2):image_height] = white
img_array[0:int(image_width / 2), 0:int(image_height / 2)] = white
print(img_array.shape)
print(img_array[int(image_width / 2), int(image_height / 2)])
print(img_array[int(image_width / 2)+3, int(image_height / 2)+3])

# Repeat the array to obtain a 400x400 chess board
img_array = np.concatenate(
    (img_array, img_array, img_array, img_array), axis=0)
img_array = np.concatenate(
    (img_array, img_array, img_array, img_array), axis=1)
print(img_array.shape)

cv2.imshow('Tabuleiro xadrez', img_array)
cv2.waitKey(0)
