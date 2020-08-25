import cv2
"""
4 pasos importantes con openCV
1.- Abrir imagen
2.- Transformar la imagen
3.- Mostrar la imagen
4.- Guardar la imagen
"""
mi_imagen = cv2.imread("necro.png", 0)     #abrirla la imagen Perla, 1 a color, 0 a grises
cv2.imshow("Mi primera imagen", mi_imagen)
cv2.imwrite("necroBN.png", mi_imagen)