"""
2)Crie uma imagem 300 x 300 e utilizando o opencv com o python
a transforme num jogo da velha com o X e 0 aonde dê empate
Sabendo:

cv2.line(imagem, ponto_inicial, ponto_final, cor, espessura)
cv2.rectangle(imagem, canto_superior_esquerdo, canto_inferior_direito, cor, espessura)
cv2.circle(imagem, ponto_centro, raio, cor, espessura)
Onde:
Ponto e canto é a coordenada do ponto(x,y)
Cor é (b, g, r)
"""

import cv2
import numpy as np

image_height = 100
image_width = 100
number_of_color_channels = 3
black = (0,0,0)
white = (255,255,255)