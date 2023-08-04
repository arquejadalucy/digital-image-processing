# Importação da biblioteca opencv
import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('paisagem.jpg')


# acessando o valor RGB do pixel 10,10
# Observação a ordem BGR e não RGB
(b, g, r) = imagem[30, 20]

# vamos mostrar a cor do pixel(10,10)

print('O pixel (30, 20) tem as seguintes cores:')

print(' Vermelho:', r, '\n Verde:   ', g, '\n Azul:    ', b)

# alterar a cor de um pixel na posição [ 10, 10 ] num quadrado
# de tamanho 5
# ( b , g, r) r = 255 g = 255 e b= 0
imagem[ 30 : 30 + 15, 20 : 20 + 15] = '#ffff00'  

# Mostra a imagem com a função imshow
cv2.imshow("Paisagem", imagem)

#espera pressionar qualquer tecla
cv2.waitKey(0)




