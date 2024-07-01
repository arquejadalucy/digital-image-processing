import cv2
import numpy as np

# lê uma imagem
img = cv2.imread('./img/mural.jpg') #Mural

# define uma matriz de cor zero (preto) de mesmo tamanho da imagem original
mascara = np.zeros(img.shape[:2], dtype = "uint8")
diferenca = np.zeros(img.shape[:2], dtype = "uint8")
complemento = np.zeros(img.shape[:2], dtype = "uint8")


# converto em cada canal
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

diferenca = b - r

v = []
for i in range(20, 90, 1):
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
for i in range(0, 100,1):
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

# Converter a imagem para o espaço de cores HSV
imagem_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir a faixa de tons de pele na escala HSV
tom_de_pele_min = np.array([0, 10, 20], dtype=np.uint8)
tom_de_pele_max = np.array([20, 255, 255], dtype=np.uint8)

# Criar uma máscara usando a faixa de tons de pele
mask = cv2.inRange(imagem_hsv, tom_de_pele_min, tom_de_pele_max)

# Extrair a parte da imagem que corresponde à pele
pele = cv2.bitwise_and(img, img, mask=mask)

roupa = cv2.bitwise_and(img, img, mask = mascara)

mascara=cv2.bitwise_or(pele, roupa)

# mostra a imagem após aplicar a máscar
cv2.imshow("Máscara aplicada à imagem", mascara)

cv2.waitKey(0)
