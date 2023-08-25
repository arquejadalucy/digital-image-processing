
import cv2

# lê uma imagem
img = cv2.imread('ipe roxo.jpg')

# mostra a imagem original
cv2.imshow("Original", img)

# faz espelhamento da imagem na horizontal
flip_horizontal = cv2.flip(img, 1)

# mostra imagem espelhada na horizontal
cv2.imshow("Flip Horizontal", flip_horizontal)

# faz espelhamento da imagem na vertical
flip_vertical = cv2.flip(img, 0)

# mostra a imagem espelhada na vertical
cv2.imshow("Flip Vertical", flip_vertical)

# faz o espelhamento da imagem na horizontal e vertical ao mesmo tempo
flip_hv = cv2.flip(img, -1)

# mostra imagem espelhada a horizontal e vertical
cv2.imshow("Flip Horizontal e Vertical", flip_hv)

cv2.waitKey(0)
