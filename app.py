import streamlit as st
import pandas as pd
from pathlib import Path

from utils.carga_datos import cargar_datos

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Dashboard ESG - ACUAMAR S.A.",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==========================================================
# RUTAS DEL PROYECTO
# ==========================================================

BASE_DIR = Path(__file__).parent

ASSETS = BASE_DIR / "assets"

LOGO = ASSETS / "logos" / "logo_acuamar.png"

BANNER = ASSETS / "banners" / "banner_esg.png"

ICONS = ASSETS / "icons"

CSS = ASSETS / "css" / "estilos.css"

# ==========================================================
# CARGAR ESTILOS CSS
# ==========================================================

def cargar_css():
    with open(CSS, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

cargar_css()

# ==========================================================
# CARGA DE DATOS
# ==========================================================

df = cargar_datos()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/240/environment-care.png",
        width=120
    )

    st.title("Dashboard ESG")

    st.markdown("### ACUAMAR S.A.")

    st.success("Proyecto Portafolio")

    st.divider()

    st.write("Versión 1.0")

# ==========================================================
# PORTADA
# ==========================================================

st.title("🌎 Dashboard ESG")

st.subheader("Evaluación ESG de ACUAMAR S.A.")

st.markdown(
"""
Bienvenido al Dashboard ESG desarrollado para evaluar el
desempeño ambiental, social y de gobernanza de ACUAMAR S.A.

Desde el menú lateral podrá acceder a cada uno de los módulos
de análisis.
"""
)

st.divider()

# ==========================================================
# INDICADORES GENERALES
# ==========================================================

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(
    "Registros",
    f"{len(df):,}"
)

kpi2.metric(
    "Variables",
    len(df.columns)
)

kpi3.metric(
    "Módulos ESG",
    5
)

st.divider()

# ==========================================================
# INFORMACIÓN DEL DATASET
# ==========================================================

col1, col2 = st.columns([2,1])

with col1:

    st.subheader("Vista previa")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

with col2:

    st.subheader("Información")

    info = pd.DataFrame({
        "Elemento":[
            "Registros",
            "Variables",
            "Valores faltantes"
        ],
        "Valor":[
            len(df),
            len(df.columns),
            int(df.isna().sum().sum())
        ]
    })

    st.dataframe(
        info,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==========================================================
# VARIABLES
# ==========================================================

st.subheader("Variables disponibles")

st.dataframe(
    pd.DataFrame(
        {"Variable":df.columns}
    ),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# MÓDULOS
# ==========================================================

st.subheader("Módulos del Dashboard")

c1, c2 = st.columns(2)

with c1:

    st.success("""
⚡ Energía

🌍 Huella de Carbono

💧 Huella Hídrica
""")

with c2:

    st.success("""
♻️ Residuos

⚠️ Riesgo Ambiental
""")

st.divider()

st.caption(
    "Desarrollado con Python • Streamlit • Plotly • Prophet"
)
