import cv2
import numpy as np

# lê uma imagem
img = cv2.imread('imagem 5.jpg')

# define uma matriz de cor zero (preto) de mesmo tamanho da imagem original
mascara = np.zeros(img.shape[:2], dtype = "uint8")
diferenca = np.zeros(img.shape[:2], dtype = "uint8")
complemento = np.zeros(img.shape[:2], dtype = "uint8")

# converte em nível de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# converto em cada canal
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

diferenca = b - r

v = []
for i in range(25,80,1):
    v.append(i)


for x in range(1, diferenca.shape[0]-1,1):
    for y in range(1,diferenca.shape[1]-1,1):
        if (diferenca[x,y] in v):
            if ((diferenca[x-1,y-1] in v) or
                (diferenca[x-1,y] in v) or
                (diferenca[x-1,y+1] in v) or
                (diferenca[x,y-1] in v) or
                (diferenca[x,y+1] in v) or
                (diferenca[x+1,y-1] in v) or
                (diferenca[x+1,y] in v)or
                (diferenca[x+1,y+1] in v)):
                mascara[x,y] = 255

complemento = 255 - (g + 110)

v = []
for i in range(20,115,1):
    v.append(i)


for x in range(1, complemento.shape[0]-1,1):
    for y in range(1,complemento.shape[1]-1,1):
        if (complemento[x,y] in v):
            if ((complemento[x-1,y-1] in v) or
                (complemento[x-1,y] in v) or
                (complemento[x-1,y+1] in v) or
                (complemento[x,y-1] in v) or
                (complemento[x,y+1] in v) or
                (complemento[x+1,y-1] in v) or
                (complemento[x+1,y] in v)or
                (complemento[x+1,y+1] in v)):
                mascara[x,y] = 255

# mostra a máscara
cv2.imshow("Máscara definida",mascara)

# aplica a máscara a imagem
# faz uma operação and da imagem com a imagem de acordo a máscara
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)

# mostra a imagem após aplicar a máscar
cv2.imshow("Máscara aplicada à imagem", img_com_mascara)


