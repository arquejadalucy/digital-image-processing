
import cv2

# lê a imagem
img = cv2.imread('ipe roxo.jpg')

# mostra a iamgem original
cv2.imshow("Original", img)

# verifica a largura e altura da imagem
largura = img.shape[1]   # eixo y nº de colunas
altura = img.shape[0]   # eixo x  nº de linhas

# é preciso calcular a proporção da altura em relação a largura da nova
# imagem, caso contrário ela poderá ficar distorcida.

proporcao = float(altura/largura)

# recalcula a nova largura com a proporção calculada
largura_nova = 300  # em pixels

# recalcula a nova altura com a proporção calculada
altura_nova = int(largura_nova*proporcao)

# define o novo tamanho (nº de colunas, nº de linhas)
tamanho_novo = (largura_nova, altura_nova)

# redimensiona a imagem mantendo a proporçao
img_redimensionada = cv2.resize(
    img, tamanho_novo, interpolation=cv2.INTER_AREA)

# mostra a imagem redimensionada
cv2.imshow('Resultado', img_redimensionada)

cv2.waitKey(0)
