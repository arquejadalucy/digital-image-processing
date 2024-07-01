import cv2
import numpy as np

#Redimensionando a imagem
# Carregue a imagem
largura, altura = 800, 600
image = cv2.imread('./img/mural.jpg')
proporcao_largura = largura / image.shape[1]
proporcao_altura = altura / image.shape[0]
proporcao = min(proporcao_largura, proporcao_altura)
nova_largura = int(image.shape[1] * proporcao)
nova_altura = int(image.shape[0] * proporcao)
imagem = cv2.resize(image, (nova_largura, nova_altura))

# HSV
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
media = cv2.bilateralFilter(hsv, 9, 75, 75)

# Esses valores podem variar dependendo da iluminação e da imagem específica
# Valores para destacar pele
low_skin = np.array([0, 20, 20], dtype=np.uint8)
high_skin = np.array([16, 255, 255], dtype=np.uint8)

# Valores para destacar roupa
low_clothing = np.array([87, 18, 30], dtype=np.uint8)
high_clothing = np.array([179, 255, 208], dtype=np.uint8)

# Criar uma máscara usando a faixa de tons de pele
mask = cv2.inRange(media, low_skin, high_skin)
mask2 = cv2.inRange(media, low_clothing, high_clothing)

# Extrair a parte da imagem que corresponde à pele
mask_skin_image = cv2.bitwise_and(imagem, imagem, mask=mask)
mask_clothing_image = cv2.bitwise_and(imagem, imagem, mask=mask2)

# Fusão das mascaras
fusion = cv2.bitwise_xor(mask_clothing_image, mask_skin_image)

# Exibição
cv2.imshow("Fusao", fusion)
# cv2.imshow("Mascara 1", mask)
# cv2.imshow("Mascara 2", mask2)

cv2.waitKey(0)