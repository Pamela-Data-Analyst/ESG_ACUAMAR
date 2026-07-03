from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO = BASE_DIR / "data" / "Datos_Sostenibilidad_Riesgos_RRHH.xlsx"

@st.cache_data
def cargar_datos():

    if not ARCHIVO.exists():
        st.error(f"No se encontró el archivo:\n\n{ARCHIVO}")
        st.stop()

    df = pd.read_excel(
        ARCHIVO,
        sheet_name="sostenibilidad"
    )

    # Limpieza de nombres de columnas
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace("\n", " ", regex=False)
    )

    return df
