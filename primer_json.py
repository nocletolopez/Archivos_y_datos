#NOTA: No colocar el nombre del archivo como "json" ya que da un error cuando se convierte
import json
from pathlib import Path

clientes = {
    
    "clientes": [
        {
            "Nombre": "Sigrid",
            "Edad": 27,
            "Cantidad": [7.17],
            "activo":True

        },
        {
            "Nombre": "Joe",
            "Edad": 31,
            "Cantidad": [
                1.9,
                5.5
            ],
            "activo":False
        },
        {
            "Nombre": "Theodoric",
            "Edad": 36,
            "Cantidad": None,
            "activo": True
            
        }
    ]
}
#Mejora el formato, es decir, aplica UFT-8
#cadena = json.dumps(clientes, ensure_ascii=False)
#print(cadena)

#Formato de impresión sin UTF-8
#cadena = json.dumps(clientes)
#print(cadena)

BASE = Path(__file__).resolve().parent
ruta = BASE / "01_Clientes.json"

#Ya no es necesario guardar esto en una variable y cerrarlo, porque utilizamos el with as
#f = open(ruta, "w", encoding= "UTF-8")
#json.dump(clientes, f, indent = 4)
#f.close()

#El with me evita utilizar el .close() y cierra todos los archivos que hayan dentro
with open(ruta,"w", encoding= "UTF-8")as f:
    json.dump(clientes, f, indent = 4)

