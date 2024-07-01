
# biblioteca de visão computação
import cv2

# plotagem das imagens geradas
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# leitura da imagem original
img = mpimg.imread('estrada.jpg')


# calcula a suavização pelo filtro bilateral
bilateral1 = cv2.bilateralFilter(img,9, 75, 75)
bilateral2 = cv2.bilateralFilter(img,9, 200, 200)


# mostra as imagens geradas

plt.figure('Borramento')

# img original
plt.subplot (1,3, 1)
plt.title ('Original')
plt.imshow (img)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pelo filtro bilateral
plt.subplot (1,3, 2)
plt.title ('bilatareal 75')
plt.imshow (bilateral1)
plt.xticks ([])
plt.yticks ([])

# tipo de suavização pelo filto bilateral
plt.subplot (1,3, 3)
plt.title ('bilatareal 200')
plt.imshow (bilateral2)
plt.xticks ([])
plt.yticks ([])

# mostra a janela criada
plt.show()
