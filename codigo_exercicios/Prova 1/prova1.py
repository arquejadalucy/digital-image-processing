"""
(Valor 10,0) A prova poderá ser realizada em grupo de no máximo 4 pessoas. 
O grupo deverá tirar 5 fotos dos integrantes do grupo e usando as técnicas apresentadas até o momento 
(histogramas, relação entre pixels, binarização e suavização) segmentar os integrantes do grupo na foto. 
Os temas das imagens deverão ter:

1) Imagem na parede de tijolos da cantina do IF

2) Imagem no reflexo de um espelho

3) Imagem na escada de metal do IF

4) Imagem tendo como fundo o moro de grama do IF

5) Imagem na frente de um mural do campus

Deverá apenas um integrante do grupo entregar a solução da prova que deverá constar:

1) Um arquivo texto com a descrição do grupo (prontuário e nome)

2) As imagens solicitadas do grupo como entrada

3) O código utilizado para efetuar a segmentação para cada imagem

4) Um arquivo texto para cada imagem descrevendo o processo utilizado para obter
a segmentação do grupo nas imagens solicitadas
"""
import cv2
import numpy as np

# lê uma imagem
img = cv2.imread('img2/parede1.jpeg')
# converte em nível de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# define uma matriz de cor zero (preto) de mesmo tamanho da imagem original
mascara = np.zeros(cinza.shape[:2], dtype = "uint8")
diferenca = np.zeros(cinza.shape[:2], dtype = "uint8")
complemento = np.zeros(cinza.shape[:2], dtype = "uint8")



# converto em cada canal
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

diferenca = b - r
complemento = 255 - (g + 110)

v = []
for i in range(15,60,1):
    v.append(i)
print("no loop 1")

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


v = []
for i in range(10,80,1):
    v.append(i)
print("no loop 2")

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

print("saí do loop 2")
cv2.imwrite("mascara.jpg", mascara)

# mostra a máscara
cv2.imshow("Máscara definida",mascara)
cv2.waitKey(0)

# aplica a máscara a imagem
# faz uma operação and da imagem com a imagem de acordo a máscara
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)
cv2.imwrite("img_com_mascara.jpg", img_com_mascara)

# mostra a imagem após aplicar a máscar
cv2.imshow("Máscara aplicada à imagem", img_com_mascara)
cv2.waitKey(0)