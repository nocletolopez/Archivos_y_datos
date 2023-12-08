from pathlib import Path
#Obtenemos la ruta para el nuevo archivo
BASE_DIR = Path(__file__).resolve().parent

#Creamos la ruta del archivo
ruta = BASE_DIR/ "archivonuevo.txt"
#print(ruta)

#Abrir el archivo en modo escritura o crearlo
f = open(ruta, "w", encoding= "UTF-8")

#Escribir texto en el archivo
f.write("Estoy usando la librería Path")

f = open (ruta, "r")
