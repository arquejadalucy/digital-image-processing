import cv2
import numpy as np
# Mais próximo de ser usando para escada
#Redimencionando a imagem
# Carregue a imagem
largura, altura = 800, 600
image = cv2.imread('./img/escada.jpg')
proporcao_largura = largura / image.shape[1]
proporcao_altura = altura / image.shape[0]
proporcao = min(proporcao_largura, proporcao_altura)
nova_largura = int(image.shape[1] * proporcao)
nova_altura = int(image.shape[0] * proporcao)
imagem = cv2.resize(image, (nova_largura, nova_altura))


# Faixa de cor laranja
lower_orange = np.array([0, 0, 100])
upper_orange = np.array([200, 255, 255])

# Faixa de cor escada
lower_brick = np.array([64, 9, 0])
upper_brick = np.array([255, 255, 255])

# Faixa de cor da pele
lower_skin = np.array([10, 43, 141])
upper_skin = np.array([13, 130, 255])

hsv_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

mask_orange = cv2.inRange(hsv_image, lower_orange, upper_orange)
mask_brick = cv2.inRange(hsv_image, lower_brick, upper_brick)
mask_skin = cv2.inRange(hsv_image, lower_skin, upper_skin)

kernel = np.ones((9, 9), np.uint8)
mask_orange = cv2.erode(mask_orange, kernel, iterations=1)
mask_orange = cv2.dilate(mask_orange, kernel, iterations=5)

mask_brick = cv2.erode(mask_brick, kernel, iterations=6)
mask_brick = cv2.dilate(mask_brick, kernel, iterations=30)

mask_skin = cv2.erode(mask_skin, kernel, iterations=1)
mask_skin = cv2.dilate(mask_skin, kernel, iterations=8)

result_orange = cv2.bitwise_and(imagem, imagem, mask=mask_orange)
result_brick = cv2.bitwise_and(imagem, imagem, mask=mask_brick)
result_skin = cv2.bitwise_and(imagem, imagem, mask=mask_skin)

orange_brick = cv2.bitwise_and(result_orange, result_skin)
fusao = cv2.bitwise_or(orange_brick, result_brick)

# Exibição
cv2.imshow('result_orange', fusao)
#cv2.imshow('result_brick', result_brick)
#cv2.imshow('result_skin', result_skin)
cv2.waitKey(0)
cv2.destroyAllWindows()
