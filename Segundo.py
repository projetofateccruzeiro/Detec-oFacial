import cv2
classificadoresFace = cv2.CascadeClassifier("cascades\\haarcascade_frontalface_default.xml")# verificar faces
classificadoresOlhos= cv2.CascadeClassifier("cascades\\haarcascade_eye.xml")#verificar olhos

imagem = cv2.imread("pessoas\\faceolho.jpg")#carrega a imagem da pasta pessoas\\nome do arquivo
imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)#converte a imagem para cinza para fazer a detecção

facesDetectadas = classificadoresFace.detectMultiScale(imagemCinza)

for(x, y, l, a)in facesDetectadas:
    imagem = cv2.rectangle(imagem, (x,y),(x+l,y+a),(0,0,2005),2)#define tamanho do retangulo e cor
    regiao=imagem[y:y+ a, x:x +l]#cria uma variavel para detectar os olhos
    regiaCinzaOlho = cv2.cvtColor(regiao,cv2.COLOR_BGR2GRAY)#converte a imagem para cinza para fazer a detecção
    olhosDetectados = classificadoresOlhos.detectMultiScale(regiaCinzaOlho,scaleFactor=1.1, minNeighbors=3,)#Ajustar parametros para melhorar se der erro em outra imagem
    print(olhosDetectados)
    for(ox, oy, ol, oa)in olhosDetectados:
        cv2.rectangle(regiao, (ox, oy),(ox + ol,oy + oa),(255,0,255),2)


cv2.imshow("Faces e Olhos Detectados",imagem)
cv2.waitKey()