import cv2
classificadoresFaces = cv2.CascadeClassifier("cascades\\haarcascade_frontalface_default.xml")
classificadoresOlhos= cv2.CascadeClassifier("cascades\\haarcascade_eye.xml")