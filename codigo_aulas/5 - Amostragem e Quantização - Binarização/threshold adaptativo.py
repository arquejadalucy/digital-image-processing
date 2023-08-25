# biblioteca de visão computacional
import cv2

# plotagem de imagens numa janela
from matplotlib import pyplot as plt

# leitura da imagem original
img = cv2.imread ( 'bingo.jpg')

# converte em nível de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret é o valor limiar (threshold) que neste caso será 127
# threshold binário
ret, thresh1 = cv2.threshold (cinza, 127,255, cv2.THRESH_BINARY)

# adaptative threshold - Média
thresh2 = cv2.adaptiveThreshold (cinza, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                             cv2.THRESH_BINARY, 25,15)

# adaptative threshold - Gaussiana
thresh3 = cv2.adaptiveThreshold (cinza, 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 25,15)




# mostra as imagens geradas

plt.figure('Binarização Adaptativa')


# img em nível de cinza
plt.subplot (2,2, 1)
plt.title ('Original')
plt.imshow (cinza, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# threshold binário
plt.subplot (2,2, 2)
plt.title ('Binary - 127')
plt.imshow (thresh1, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# adaptative threshold média
plt.subplot (2,2, 3)
plt.title ('Adaptativa - Média')
plt.imshow (thresh2, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# adaptative threshold gaussiana
plt.subplot (2,2, 4)
plt.title ('Adaptativa - Gaussiana')
plt.imshow (thresh3, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])


plt.show ()
