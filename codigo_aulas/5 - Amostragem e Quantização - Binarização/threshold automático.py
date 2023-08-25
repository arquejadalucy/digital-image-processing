import cv2

from matplotlib import pyplot as plt


img = cv2.imread ( 'estrada com arvores.jpg')

# converte em nível de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret é o valor limiar (threshold) que neste caso será 127
# threshold binário
ret1, thresh1 = cv2.threshold (cinza, 127,255, cv2.THRESH_BINARY)

# otsu threshold
ret2, thresh2 = cv2.threshold (cinza, 0,255, cv2.THRESH_BINARY +
                               cv2.THRESH_OTSU)

# triangle threshold
ret3, thresh3 = cv2.threshold (cinza, 0,255, cv2.THRESH_BINARY +
                               cv2.THRESH_TRIANGLE)


# mostra as imagens geradas

plt.figure('Binarização Automática')


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

# Otsu threshold 
plt.subplot (2,2, 3)
plt.title ('Threshold Otsu')
plt.imshow (thresh2, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

# triangle threshold 
plt.subplot (2,2, 4)
plt.title ('Threshold Triangle')
plt.imshow (thresh3, 'gray' , vmin = 0, vmax = 255)
plt.xticks ([])
plt.yticks ([])

plt.show ()

print('limiar binario: ', ret1, 'limiar Otsu: ',ret2, 'limiar triângulo: ',ret3)
