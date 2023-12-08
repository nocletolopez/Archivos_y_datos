from pathlib import Path
#Creo u obtengo la ruta del nuevo archivo
BASE = Path(__file__).resolve().parent
#Creo el anombre del archivo y asigno su ruta
RUTA_ARCHIVO = BASE / "Hobbiesfavoritos.txt"
#Creo o inicializo el archivo
f = open(RUTA_ARCHIVO, "w", encoding="UTF-8")
#Solicito datos al usuario
print("Ingrese un hobbie de su preferencia: ")
#bucle para solicitar tres veces
for i in range(3):
    dato = input()
    f.write(dato + "\n")
f.close

