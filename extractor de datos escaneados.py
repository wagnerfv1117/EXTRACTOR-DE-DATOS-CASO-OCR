# 1-Se importan las siguientes librerías que son necesarias para la tarea
import pytesseract as tess #  librería que se encarga de todo el procesamiento de imágenes, por medio de procesamiento optico de caracteres (OCR) por sus siglas en inglés
from PIL import Image # librería PILLOW la cual ayuda con su modulo Image para que se puedan visualizar las imagenes
import cv2 # modulo de la ibrería openCV que ayuda a vision artificial de imagenes
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Es una API  de Google, se debe instalar el ejecutable de windows en el computador o según sea el caso en otro SO - https://tesseract-ocr.github.io/tessdoc/Installation.html

# 2-Se hacen los respectivos metodos y strings para ubicar y leer el archivo de imagen (.jpg)
my_image = cv2.imread('C:/Users/wagne/OneDrive - POLICIA NACIONAL DE COLOMBIA/Documents/PROYECTOS CIENCIA DE DATOS/EXTRACTOR DE DATOS CASO OCR/input/imagen1.jpg')#ojo siempre cambiar la ruta de acceso
txt = tess.image_to_string(my_image)#Se hace un string para que la librería pytessract haga el reconocimiento de caracteres en la imgen o escaneado
print(txt)#Se imprime la variable txt, definida anteriormente

# 3-Metodo para que muestre la imagen después de leerla
cv2.imshow('Image', my_image)#Metodo para que la maquina muestre la imagen
cv2.waitKey(0)#El contador para mostrar la imagen analizada
cv2.destroyAllWindows()#Apertura en una ventana con insterfaz del Sistema Operativo

# 4-Se define unas variables y métodos, para que el texto tomado la imagen por reconocimiento de caracteres, se guarde en un documento .txt
my_file = open('output/datos.txt', 'w')#variable para la creación de un archivo en formato .txt o de texto
my_file.write(txt + '\n')#variable para que los datos capturados sean guardados en eun archivo .txt o de texto
my_file.close()#el programa finaliza su proceso


