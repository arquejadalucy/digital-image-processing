import cv2

# leitura da imagem a qual vamos calcular o histotgrama
img = cv2.imread('imagem 5.jpg')

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# converte em nível de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('Cinza.jpg',cinza)
cv2.imwrite('azul.jpg',b)
cv2.imwrite('verde.jpg',g)
cv2.imwrite('vermelha.jpg',r)


