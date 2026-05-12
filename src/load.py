from sqlalchemy.engine import Engine
import pandas as pd

def cargar_tabla(tabla_origen: pd.DataFrame, tabla_destino: str, motor: Engine)-> None:

    tabla_origen.to_sql(name=tabla_destino, con=motor, if_exists='replace', schema='dw', index=False)