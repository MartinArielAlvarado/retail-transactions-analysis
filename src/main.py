import extract
import transform
import load

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

def validar_tabla(tabla1: pd.DataFrame, columna_key: str)->None:

    try:
        assert len(tabla1) == tabla1[columna_key].nunique()
    except AssertionError:
        print(f"Error DQ: Claves duplicadas")
        raise


def run_pipeline()->None:

    motor: Engine = create_engine('postgresql://martin:admin123@localhost:5432/transactions_db')

    datos_crudos: pd.DataFrame = extract.extraer_datos_crudos()
    dim_product: pd.DataFrame = transform.crear_dim_product(datos_crudos)
    dim_store: pd.DataFrame = transform.crear_dim_store(datos_crudos)
    dim_payment: pd.DataFrame = transform.crear_dim_payment(datos_crudos)
    dim_transactionDate: pd.DataFrame = transform.crear_dim_transactionDate(datos_crudos)
    dim_transactionTime: pd.DataFrame = transform.crear_dim_transactionTime(datos_crudos)
    fact_transactions: pd.DataFrame = transform.crear_fact_transactions(datos_crudos, dim_product, dim_store, dim_payment, dim_transactionDate, dim_transactionTime)

    validar_tabla(dim_product, "Product_key")
    validar_tabla(dim_store, "Store_key")
    validar_tabla(dim_payment, "Payment_key")
    validar_tabla(dim_transactionDate, "Date_key")
    validar_tabla(dim_transactionTime, "Time_key")

    load.cargar_tabla(dim_product, 'dim_product', motor)
    load.cargar_tabla(dim_store, 'dim_store', motor)
    load.cargar_tabla(dim_payment, 'dim_payment', motor)
    load.cargar_tabla(dim_transactionDate, 'dim_transactionDate', motor)
    load.cargar_tabla(dim_transactionTime, 'dim_transactionTime', motor)
    load.cargar_tabla(fact_transactions, 'fact_transactions', motor)

if __name__ == '__main__':
    run_pipeline()