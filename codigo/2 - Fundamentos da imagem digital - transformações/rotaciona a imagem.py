import cv2

# lê imagem
imagem = cv2.imread('ipe roxo.jpg')

# Mostra a imagem original
cv2.imshow("Original", imagem)

# verificando a altura, largura da imagem
altura = imagem.shape[0]    # nº de linhas
largura = imagem.shape[1]    # nº de colunas

# encontra o raio da imagem
# // divisão inteira
centro = (largura // 2, altura // 2)

# gera a matriz de rotação da imagem em 45 graus
M = cv2.getRotationMatrix2D(centro, 45, 1.0)

# realiza a rotação da imagem em 45 graus
img_rotacionada = cv2.warpAffine(imagem, M, (largura, altura))

# mostra a imagem rotacionada
cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)

cv2.waitKey(0)
