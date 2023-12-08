import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ruta = BASE / "01_Clientes.json"

#Si el archivo json no está dentro de la carpeta o ruta, da error ya que no puede leer algo que no esté dentro de donde se le espcifica
with open(ruta, encoding= "UTF-8") as f:
   #El load carga el archoivo y lo guarda en una variable
   lectura_datos = json.load(f)

#Recorro la lista de clientes (lista) y la analizo con su clave y valor
for cliente in lectura_datos["clientes"]:
    print("Nombre completo: ", cliente["Nombre"])
    print("Edad: ", cliente["Edad"])
    if cliente["Cantidad"]:
        #El len cuenta cuántos elementos tiene la lista
        print("Cantidad de pedidos: ", len(cliente["Cantidad"]))
    else:
        print("No tiene pedidos")
    if cliente["activo"]:
        print("Cliente activo:  Sí")
    else:
        print("Cliente activo: No")
    
    print()
    

    
    

