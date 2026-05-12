import pandas as pd
from pathlib import Path

def extraer_datos_crudos():

    ruta_script = Path(__file__).resolve()

    carpeta_src = ruta_script.parent

    raiz_proyecto = carpeta_src.parent

    ruta_archivo = raiz_proyecto / "data" / "raw" / "Retail_Transaction_Dataset.csv"

    dataset = pd.read_csv(ruta_archivo)

    return dataset