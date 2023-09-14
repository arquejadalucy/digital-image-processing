"""
2)Crie uma imagem 300 x 300 e utilizando o opencv com o python
a transforme num jogo da velha com o X e 0 aonde dê empate
Sabendo:

cv2.line(imagem, ponto_inicial, ponto_final, cor, espessura)
cv2.circle(imagem, ponto_centro, raio, cor, espessura)
cv2.rectangle(imagem, canto_superior_esquerdo,
              canto_inferior_direito, cor, espessura)
Onde:
Ponto e canto é a coordenada do ponto(x,y)
Cor é (b, g, r)
"""

import cv2
import numpy as np

image_height = 300
image_width = 300
number_of_color_channels = 3
black = (0, 0, 0)
white = (255, 255, 255)

# Creating 300x300 white image
img_array = np.full(
    (image_height, image_width, number_of_color_channels),
    white, dtype=np.uint8)

for i in [100, 200]:
    cv2.line(img_array, [i, 0], [i, 300], black,
             thickness=3, lineType=cv2.LINE_4, shift=0)
    cv2.line(img_array, [0, i], [300, i], black,
             thickness=3, lineType=cv2.LINE_4, shift=0)

"""
| x | 0 | x |
| 0 | x | x |
| 0 | x | 0 |
"""
coordenadas_dos_x = [
    [[10, 10], [90, 90], [90, 10], [10, 90]],
    [[210, 10], [290, 90], [290, 10], [210, 90]],
    [[110, 110], [190, 190], [110, 190], [190, 110]],
    [[210,110], [290, 190], [210, 190], [290, 110]],
    [[110, 210], [190, 290], [110, 290], [190, 210]]
]

centros_dos_O = [
    [150, 50],
    [50, 150],
    [50, 250],
    [250, 250]
]

for [a, b, c, d] in coordenadas_dos_x:
    cv2.line(img_array, a, b, black,
             thickness=1, lineType=cv2.LINE_4, shift=0)
    cv2.line(img_array, c, d, black,
             thickness=1, lineType=cv2.LINE_4, shift=0)

for centro in centros_dos_O:
    cv2.circle(img_array, centro, 40, black, thickness=1)

cv2.imshow('Jogo da velha', img_array)
cv2.waitKey(0)
