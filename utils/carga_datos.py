"""
====================================================
Módulo: carga_datos.py
Proyecto: Dashboard ESG - ACUAMAR S.A.
Autor: Pamela Herrera
====================================================
"""

from pathlib import Path
import pandas as pd
import streamlit as st


#-----------------------------------------------------
# Ruta del archivo Excel
#-----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

ARCHIVO_EXCEL = BASE_DIR / "data" / "Datos_Sostenibilidad_Riesgos_RRHH.xlsx"


#-----------------------------------------------------
# Lectura del archivo
#-----------------------------------------------------

@st.cache_data(show_spinner="Cargando información...")
def cargar_datos():

    if not ARCHIVO_EXCEL.exists():

        st.error(
            f"""
            No se encontró el archivo:

            {ARCHIVO_EXCEL}

            Verifique que el archivo Excel esté dentro de la carpeta:

            data/
            """
        )

        st.stop()

    df = pd.read_excel(
        ARCHIVO_EXCEL,
        sheet_name="sostenibilidad"
    )

    return df
