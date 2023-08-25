import cv2

# lê uma imagem
imagem = cv2.imread('ipe roxo.jpg')

# mostra a imagem original
cv2.imshow("Imagem Original", imagem)

# faz o recore  na área (200,350) à (300,450)
recorte = imagem[200:300, 300:450]

# mostra a imagem recortada
cv2.imshow("Recorte da imagem", recorte)

# salva a imagem recortada no disco
cv2.imwrite("recorte.jpg", recorte)

cv2.waitKey(0)
