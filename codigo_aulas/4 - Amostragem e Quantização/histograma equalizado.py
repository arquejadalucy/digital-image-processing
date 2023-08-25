# para fazer a plotagem do histograma
from matplotlib import pyplot as plt

# para as função de manipulação de imagens
import cv2

# faz a leitura da imagem
img = cv2.imread('imagem 5.jpg')

# converte a imagem em nível de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# realza a equalização da imagem
cinza_eq = cv2.equalizeHist(img[:,:,2])

# mostra as imagens em nível de cinza e equalizada
cv2.imshow('Imagem Original',cinza)
cv2.imshow('Imagem Equalizada',cinza_eq)

# plotar o histograma da imagem equalizda
plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(cinza_eq.ravel(), 256, [0,255])
plt.xlim([0, 256])
plt.show()

# plotar o histograma da imagem em cinza
plt.figure() # cria uma janela
plt.title("Histograma Original")  # título do gráfico
plt.xlabel("Intensidade")   # título do eixo x
plt.ylabel("Qtde de Pixels") # título do eixo y
plt.hist(cinza.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()
