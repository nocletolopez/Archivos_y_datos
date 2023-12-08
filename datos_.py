from pathlib import Path
import pandas

BASE = Path(__file__).resolve().parent
ruta = BASE / "dataset_turnos_detalle.csv"

datos = pandas.read_csv(ruta)