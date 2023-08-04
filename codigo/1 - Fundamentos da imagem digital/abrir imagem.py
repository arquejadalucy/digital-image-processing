# importação da biblioteca opencv
import cv2

# imread = image read = ler imagem
imagem = cv2.imread('lenna.jpg')

# imshow = image show = mostrar imagem
# mostra numa janela dessa forma, imshow(titulo da janela, imagem)
cv2.imshow("Lenna", imagem[:, :, 2])
# canal 2 é o canal R (red - vermelho)
# canal 1 é o canal G (green - verde)
# canal 0 é o canal B (blue - blue)


# espera-se até que uma tecla seja pressionada
cv2.waitKey(0)

# imwrite = image write = salvar imagem
# imwrite(nome do arquivo, variável que contém a imagem)
cv2.imwrite("saida_r.jpg", imagem[:, :, 2])
