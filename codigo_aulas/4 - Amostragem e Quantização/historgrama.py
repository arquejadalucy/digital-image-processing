# bilbiote para as funções de visão computacinal
import cv2

# para plotagem do Histograma
from matplotlib import pyplot as plt

# leitura da imagem a qual vamos calcular o histotgrama
img = cv2.imread('catedral.jpg')

# converte em nível de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Nivel de cinza',cinza)


#Função calcHist para calcular o hisograma da imagem
h = cv2.calcHist([cinza], [0], None, [256], [0, 255])

# cria uma figura (janela)
plt.figure('Histograma')  # título da janela
plt.title("Histograma em nivel de cinza")  # título do gráfico
plt.xlabel("Intensidade")
plt.xlim([0, 255])
plt.ylabel("Qtde de Pixels")
plt.plot(h) # ou plt.hist(cinza.ravel(),256,[0,256])
plt.show()




