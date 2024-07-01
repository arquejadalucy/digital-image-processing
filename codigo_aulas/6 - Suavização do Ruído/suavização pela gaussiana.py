
# biblioteca de visão computação
import cv2

# plotagem das imagens geradas
from matplotlib import pyplot as plt

# leitura da imagem original
img = cv2.imread('flores.jpg')


# calcula a suavização pela gaussiana
gaus = cv2.GaussianBlur(img,(5,5), 0)

# mostra as imagens geradas

plt.figure('Borramento')

# img original
plt.subplot (1,2, 1)
plt.title ('Original')
plt.imshow (img)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela gaussiana
plt.subplot (1,2, 2)
plt.title ('Gaussiana')
plt.imshow (gaus)
plt.xticks ([])
plt.yticks ([])

# mostra a janela criada
plt.show()
