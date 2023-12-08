from pathlib import Path
#Obtenemos la ruta para el nuevo archivo
BASE_DIR = Path(__file__).resolve().parent

#Creamos la ruta del archivo
ruta = BASE_DIR/ "textorepetido.txt"
#print(ruta)

#Abrir el archivo en modo escritura o crearlo
f = open(ruta, "a", encoding= "UTF-8")
#"ejecuta el programa 5 veces"
for i in range(5):
    #Escribir texto en el archivo
    f.write("Estoy usando la librería Path\n")
f.close()

otras_lineas = ("uno", "dos", "tres", "cuatro")
f.writelines(otras_lineas)
f.close()