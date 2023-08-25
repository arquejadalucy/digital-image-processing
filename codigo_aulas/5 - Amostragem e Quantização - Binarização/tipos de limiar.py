# bilbioteca para execução do processamento digital da imagem
import cv2

# plotagem das imagens geradas
from matplotlib import pyplot as plt

# imagem
img = cv2.imread ( 'gradiente.jpg')

# converte em nível de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret é o valor limiar (threshold) que neste caso será 127
ret, thresh1 = cv2.threshold (cinza, 127,255, cv2.THRESH_BINARY)
print('binario =',ret)
ret, thresh2 = cv2.threshold (cinza, 127,255, cv2.THRESH_BINARY_INV)
print('binario invertido =',ret)
ret, thresh3 = cv2.threshold (cinza, 127,255, cv2.THRESH_TRUNC)
print('truncado =',ret)
ret, thresh4 = cv2.threshold (cinza, 127,255, cv2.THRESH_TOZERO)
print('to zero =',ret)
ret, thresh5 = cv2.threshold (cinza, 127,255, cv2.THRESH_TOZERO_INV)
print('to zero invertido =',ret)

# mostra as imagens geradas

# define uma nova janela
plt.figure('Binarização')

# img em nível de cinza
plt.subplot (2,3, 1)
plt.title ('Original')
plt.imshow (cinza, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# tipo de limiar binary
plt.subplot (2,3, 2)
plt.title ('Binary')
plt.imshow (thresh1, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# tipo de limiar binary_inv
plt.subplot (2,3, 3)
plt.title ('Binary_inv')
plt.imshow (thresh2, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# tipo de limiar trunc
plt.subplot (2,3, 4)
plt.title ('Trunc')
plt.imshow (thresh3, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# tipo de limiar tozero
plt.subplot (2,3, 5)
plt.title ('ToZero')
plt.imshow (thresh4, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# tipo de limiar trunc
plt.subplot (2,3, 6)
plt.title ('ToZero_inv')
plt.imshow (thresh5, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])


plt.show ()



