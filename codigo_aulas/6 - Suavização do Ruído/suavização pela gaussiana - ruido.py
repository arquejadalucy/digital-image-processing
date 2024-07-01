

# biblioteca de visão computação
import cv2

# plotagem das imagens geradas
from matplotlib import pyplot as plt

# leitura da imagem original
img = cv2.imread('ruido.jpg')


# calcula a suavização pela gaussiana
gaus1 = cv2.GaussianBlur(img,(3,3),0)
gaus2 = cv2.GaussianBlur(img,(5,5),0)
gaus3 = cv2.GaussianBlur(img,(7,7),0)

# mostra as imagens geradas

plt.figure('Borramento')

# img original
plt.subplot (2,2, 1)
plt.title ('Original')
plt.imshow (img)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela gaussiana
plt.subplot (2,2, 2)
plt.title ('Gaussian 3x3')
plt.imshow (gaus1)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela gaussiana
plt.subplot (2,2, 3)
plt.title ('Gaussiana 5x5')
plt.imshow (gaus2)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela gaussiana
plt.subplot (2,2, 4)
plt.title ('Gaussiana 7x7')
plt.imshow (gaus3)
plt.xticks ([])
plt.yticks ([])

# mostra a janela criada
plt.show()
