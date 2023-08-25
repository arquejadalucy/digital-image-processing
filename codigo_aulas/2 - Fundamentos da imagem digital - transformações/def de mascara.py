import cv2
import numpy as np

# lê uma imagem
img = cv2.imread('ipe roxo.jpg')

# mosra a imagem original
cv2.imshow("Original", img)

# define uma matriz de cor zero (preto) de mesmo tamanho da imagem original
mascara = np.zeros(img.shape[:2], dtype="uint8")

# calcula o centro da imagem original
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)

# define a parte ligada (pixels brancos da máscara)
# 100 indica o raio do círculo
# 255 a cor branca (nível de cinza)
# -1 indica que a espessura será a parte interna do cículo
cv2.circle(mascara, (cX, cY), 100, 255, -1)

# mostra a máscara
cv2.imshow("Máscara definida", mascara)

# aplica a máscara a imagem
# faz uma operação and da imagem com a imagem de acordo a máscara
img_com_mascara = cv2.bitwise_and(img, img, mask=mascara)

# mostra a imagem após aplicar a máscar
cv2.imshow("Máscara aplicada à imagem", img_com_mascara)

cv2.waitKey(0)
