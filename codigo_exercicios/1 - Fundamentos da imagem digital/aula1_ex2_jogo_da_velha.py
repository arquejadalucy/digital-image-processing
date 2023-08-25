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


for [i, j] in [[0, 0], [200, 0], [100, 0]]:
    cv2.line(img_array, [i, j], [i + 100, j + 100], black,
             thickness=1, lineType=cv2.LINE_4, shift=0)
    cv2.line(img_array, [i + 100, j], [i, j + 100], black,
             thickness=1, lineType=cv2.LINE_4, shift=0)
#
# cv2.line(img_array, [200, 0], [300, 100], black,
#          thickness=1, lineType=cv2.LINE_4, shift=0)
# cv2.line(img_array, [300, 0], [200, 100], black,
#          thickness=1, lineType=cv2.LINE_4, shift=0)
#
# cv2.line(img_array, [100, 100], [200, 200], black,
#          thickness=1, lineType=cv2.LINE_4, shift=0)
# cv2.line(img_array, [100, 200], [200, 100], black,
#          thickness=1, lineType=cv2.LINE_4, shift=0)

"""
| x | 0 | x |
| 0 | x | x |
| 0 | x | 0 |
"""
coordenadas_dos_x = {
    1: [[0, 0], [100, 100], [100, 0], [0, 100]],
    2: [[200, 0], [300, 100], [300, 0], [200, 100]],
    3: [[100, 100], [200, 200], [100, 200], [200, 100]],
    #4: [[i, j], [i+100, j+100], [j+100, j], [i, j+100]]
    # 4: [[200,100], [300, 200], []]
}

cv2.imshow('Jogo da velha', img_array)
cv2.waitKey(0)
