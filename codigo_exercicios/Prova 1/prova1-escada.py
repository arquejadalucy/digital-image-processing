import cv2
import numpy as np

# lê uma imagem
# img = cv2.imread('mural.jpg') #Mural
img = cv2.imread('img/imagem2.png')  # Grama

# gaus = cv2.GaussianBlur(img, (9,9), 9)
# define uma matriz de cor zero (preto) de mesmo tamanho da imagem original
mascara = np.zeros(img.shape[:2], dtype="uint8")
diferenca = np.zeros(img.shape[:2], dtype="uint8")
complemento = np.zeros(img.shape[:2], dtype="uint8")

# converte em nível de cinza
# cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# converto em cada canal
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

diferenca = b - r

v = []
for i in range(10, 50, 1):
    v.append(i)

for x in range(1, diferenca.shape[0] - 1, 1):
    for y in range(1, diferenca.shape[1] - 1, 1):
        if (diferenca[x, y] in v):
            if ((diferenca[x - 1, y - 1] in v) or
                    (diferenca[x - 1, y] in v) or
                    (diferenca[x - 1, y + 1] in v) or
                    (diferenca[x, y - 1] in v) or
                    (diferenca[x, y + 1] in v) or
                    (diferenca[x + 1, y - 1] in v) or
                    (diferenca[x + 1, y] in v) or
                    (diferenca[x + 1, y + 1] in v)):
                mascara[x, y] = 255

complemento = 255 - (g + 110)

v = []
for i in range(90, 100, 1):
    v.append(i)

for x in range(1, complemento.shape[0] - 1, 1):
    for y in range(1, complemento.shape[1] - 1, 1):
        if (complemento[x, y] in v):
            if ((complemento[x - 1, y - 1] in v) or
                    (complemento[x - 1, y] in v) or
                    (complemento[x - 1, y + 1] in v) or
                    (complemento[x, y - 1] in v) or
                    (complemento[x, y + 1] in v) or
                    (complemento[x + 1, y - 1] in v) or
                    (complemento[x + 1, y] in v) or
                    (complemento[x + 1, y + 1] in v)):
                mascara[x, y] = 255

# Converter a imagem para o espaço de cores HSV
# imagem_hsv = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)
imagem_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir a faixa de tons de pele na escala HSV
# Esses valores podem variar dependendo da iluminação e da imagem específica
tom_de_pele_min = np.array([0, 10, 20], dtype=np.uint8)
tom_de_pele_max = np.array([20, 255, 255], dtype=np.uint8)

# Criar uma máscara usando a faixa de tons de pele
mask = cv2.inRange(imagem_hsv, tom_de_pele_min, tom_de_pele_max)

# Extrair a parte da imagem que corresponde à pele
pele = cv2.bitwise_and(img, img, mask=mask)

# Mostrar a imagem da pele isolada
# cv2.imshow('Pele Isolada', imagem_pele)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Salvar a imagem da pele isolada
# cv2.imwrite('pele_isolada.jpg', imagem_pele)

# mostra a máscara
# cv2.imshow("Máscara definida",mascara)

# aplica a máscara a imagem
# faz uma operação and da imagem com a imagem de acordo a máscara
roupa = cv2.bitwise_and(img, img, mask=mascara)

mascara = cv2.bitwise_or(pele, roupa)
cv2.imwrite("escada.jpeg", mascara)
# mostra a imagem após aplicar a máscar
cv2.imshow("Máscara aplicada à imagem", mascara)

cv2.waitKey(0)
