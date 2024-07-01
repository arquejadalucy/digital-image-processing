
# biblioteca de visão computação
import cv2

# plotagem das imagens geradas
from matplotlib import pyplot as plt

# leitura da imagem original
img = cv2.imread('ruido.jpg')


# calcula a suavização pela média
media1 = cv2.blur(img,(3,3))
media2 = cv2.blur(img,(5,5))
media3 = cv2.blur(img,(7,7))

# mostra as imagens geradas

plt.figure('Borramento')

# img original
plt.subplot (2,2, 1)
plt.title ('Original')
plt.imshow (img)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela média
plt.subplot (2,2, 2)
plt.title ('Media 3x3')
plt.imshow (media1)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela média
plt.subplot (2,2, 3)
plt.title ('Media 5x5')
plt.imshow (media2)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pela média
plt.subplot (2,2, 4)
plt.title ('Media 7x7')
plt.imshow (media3)
plt.xticks ([])
plt.yticks ([])

# mostra a janela criada
plt.show()
