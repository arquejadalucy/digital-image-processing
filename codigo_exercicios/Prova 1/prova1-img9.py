import cv2
import numpy as np

# Função para ajustar os parâmetros
def nothing(x):
    pass

# Crie uma janela com controles deslizantes para ajustar os parâmetros
cv2.namedWindow('Segmentation Parameters')
cv2.createTrackbar('Low H', 'Segmentation Parameters', 0, 255, nothing)
cv2.createTrackbar('Low S', 'Segmentation Parameters', 0, 255, nothing)
cv2.createTrackbar('Low V', 'Segmentation Parameters', 0, 255, nothing)
cv2.createTrackbar('High H', 'Segmentation Parameters', 179, 179, nothing)
cv2.createTrackbar('High S', 'Segmentation Parameters', 255, 255, nothing)
cv2.createTrackbar('High V', 'Segmentation Parameters', 255, 255, nothing)

# Carregue a imagem
image = cv2.imread('img2/escada2.jpeg')
input_size = (1000, 600)
imagem = cv2.resize(image, input_size)
while True:
    # Capture os valores dos controles deslizantes
    low_h = cv2.getTrackbarPos('Low H', 'Segmentation Parameters')
    low_s = cv2.getTrackbarPos('Low S', 'Segmentation Parameters')
    low_v = cv2.getTrackbarPos('Low V', 'Segmentation Parameters')
    high_h = cv2.getTrackbarPos('High H', 'Segmentation Parameters')
    high_s = cv2.getTrackbarPos('High S', 'Segmentation Parameters')
    high_v = cv2.getTrackbarPos('High V', 'Segmentation Parameters')

    # Crie uma imagem HSV
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Defina os limites da cor da pele com base nos valores dos controles deslizantes
    lower_skin = np.array([low_h, low_s, low_v], dtype=np.uint8)
    upper_skin = np.array([high_h, high_s, high_v], dtype=np.uint8)

    # Aplique a máscara de segmentação
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Aplique a máscara na imagem original
    segmented = cv2.bitwise_and(imagem, imagem, mask=mask)

    # Exiba a imagem segmentada
    cv2.imshow('Segmented Image', segmented)

    # Aguarde a tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere os recursos
cv2.destroyAllWindows()