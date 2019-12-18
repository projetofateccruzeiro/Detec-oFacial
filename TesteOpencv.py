import cv2

print(cv2)

image = cv2.imread("opencv-python.jpg")#cria variavel da imagem
imagecinza= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#muda a imagem de cor
imagefatec = cv2.imread("FATEC3.jpg")
cv2.imshow("Original",image)#mostra a imagem
cv2.imshow("Cinza",imagecinza)#mostra a imagem
cv2.imshow("Fatec",imagefatec)
cv2.waitKey()#teclando qualquer tecla fecha as imagens