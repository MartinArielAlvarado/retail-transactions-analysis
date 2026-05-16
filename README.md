# Pipeline End-to-End de Transacciones de Retail (EDA | Data Warehouse | ETL | Power BI)🛒

**Proyecto de Business Intelligence integral enfocado en analisis de transacciones de retail, modelado y visualizacion de datos en Power BI.**

## 🎯 Contexto del Proyecto
Este proyecto cuenta con 3 etapas:

1. EDA: Analisis exploratorio del dataset (tipo "sabana") en Jupyter Notebook utilizando Pandas y Matplotlib (seabron.objects), ademas de consultas SQL (PostgreSQL y Dbeaver) comentadas con el objetivo de tener un primer acercamiento a la informacion que contiene (tipos de datos, estadistica descriptiva, visualizaciones, calidad y patrones).
2. Modelado y ETL: Para el diseno del DW se sigue el 'Star Schema' de Kimball creando tablas de Dimensiones y Hechos (Dim-Fact) que facilitan el desarrollo de dashboards en Power BI y optimizan tiempos de consulta. El ETL cuenta con 4 archivos en Python separando responsabilidades de extraccion, transformacion y carga de 100000 transacciones ademas de un archivo main.py para orquestarlos. Todo fue desarrollado integramente en un entorno WSL (Ubuntu), VScode y Git. 
3. Visualiaciones y BI: Diseno y desarrollo de dashboards interactivos en Power BI para la toma de decisiones estategicas.

## 🛠️ Stack Tecnológico
* **Procesamiento y Análisis:** Python (Pandas), SQL, DAX
* **Visualización de Datos:** Matplotlib, Seaborn (`seaborn.objects`), Power BI
* **Entorno:** Jupyter Notebook, Git, WSL (Ubuntu).

---

## 💡 Resumen Ejecutivo (Hallazgos Principales)

* **Horarios de mayor actividad vs. Recaudación:** Se observó que el pico de transacciones ocurre a las 19:00 hs (impulsado por la categoría *Home Decor*), sin embargo, la hora que genera mayores ingresos brutos es a la 01:00 hs. Esto es sobre el historico de las transacciones y varia segun las fechas. En el dashboard interactivo de Power BI se pueden modificar las fechas y ver que existen momentos de consumo variable que permitirian un analisis de estacionalidad y habitos de consumo mas detallado en un ambito real.
  * *Oportunidad detectada:* Ofrecer descuentos en horarios de baja actividad podría simplemente trasladar las ventas que igual iban a ocurrir en el horario pico, sin generar ingresos nuevos. Una alternativa más rentable sería aprovechar el tráfico natural de las 19:00 hs ofreciendo beneficios (como envío bonificado) a partir de un ticket de compra más alto.
* **Segmentación de Clientes (Modelo RFM):** Agrupando a los clientes por su Recencia, Frecuencia y Valor Monetario, se determinó que aproximadamente un 95% de los clientes compraron una sola vez y al cruzar esta informacion con el analisis de concentracion de revenue resulta en que aproximadamente el 50% de los clientes concentran el 80% del revenue.
* **Comportamiento por Medio de Pago:** Los datos muestran que los usuarios no presentan grandes diferencias entre metodos de pago, resultan en montos similares (teniendo en cuenta que es un dataset ficticio descargado de Kaggle).

---

## 🏗️ Modelo y Tablas

El esquema Estrella esta compuesto por las siguientes tablas y un contenedor logico dw:

* **Dimensional: dim_product, dim_store, dim_payment, dim_transactionDate, dim_transactionTime
* **Fact:fact_transactions

placeholder imagen esquema!!!

---

## 📂 Estructura del Repositorio

```text
retail-transactions-analysis/
│
├── dashboards/
│   └── analisis_transacciones.pbix                   # Archivo de Power BI
├── data/
│   ├── raw/                                          # Dataset original
│   └── processed/                                    # Dataset limpio listo para BI
├── database/
|   └── db_setup/                                     # Archivos .sql de schema y tablas
├── images/
│   |── KPIs_ventas_metodo_pago.png                   # Capturas de dashboards
│   |── ventas_horas_dias.png                         # Capturas de dashboards
│   |── RFM_clientes_historico.png                    # Capturas de dashboards
|   └── diagrama_db_retail_transactions_analysis.png  # Imagen de la bd                          
├── notebooks/
│   └── analisis_visual.ipynb                         # Código fuente: Limpieza, EDA y Modelo RFM
├── src/                                              # Archivos .py del ETL
├── README.md
├── requirements.txt
└── .gitignore
