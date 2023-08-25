
import cv2

imagem = cv2.imread('paisagem.jpg')

cv2.imshow("Paisagem", imagem)

(b, g, r) = imagem[30, 20]

print('O pixel (30, 20) tem as seguintes cores:')

print(' Vermelho:', r, '\n Verde:   ', g, '\n Azul:    ', b)

cv2.waitKey(0)




