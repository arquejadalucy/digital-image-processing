
# biblioteca de visão computação
import cv2

# plotagem das imagens geradas
from matplotlib import pyplot as plt

# leitura da imagem original
img = cv2.imread('flores.jpg')


# calcula a suavização pela média
media = cv2.blur(img,(5,5))

# calcula a suavização pela gaussiana
gaus = cv2.GaussianBlur(img,(5,5), 0)

# calcula a suavização pela mediana
mediana = cv2.medianBlur(img,5)

# mostra as imagens geradas

plt.figure('Borramento')

# img original
plt.subplot (1,4, 1)
plt.title ('Original')
plt.imshow (img)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela média
plt.subplot (1,4, 2)
plt.title ('Média')
plt.imshow (media)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela gaussiana
plt.subplot (1,4, 3)
plt.title ('Gaussiana')
plt.imshow (gaus)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela média
plt.subplot (1,4, 4)
plt.title ('Mediana')
plt.imshow (mediana)
plt.xticks ([])
plt.yticks ([])


# mostra a janela criada
plt.show()
