# ==========================================================
# HEADER CORPORATIVO
# Dashboard ESG - ACUAMAR S.A.
# ==========================================================

import streamlit as st
from pathlib import Path
from datetime import datetime


# ==========================================================
# RUTAS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

LOGO = BASE_DIR / "assets" / "logos" / "logo_acuamar.png"


# ==========================================================
# HEADER
# ==========================================================

def mostrar_header():

    fecha = datetime.now().strftime("%d/%m/%Y")

    col_logo, col_info, col_fecha = st.columns([1,5,1.5])

    # ------------------------------------------------------

    # LOGO

    # ------------------------------------------------------

    with col_logo:

        st.image(LOGO, width=90)

    # ------------------------------------------------------

    # TITULOS

    # ------------------------------------------------------

    with col_info:

        st.markdown(
            """
            <div class="header-title">
                Dashboard ESG Corporativo
            </div>

            <div class="header-subtitle">
                Evaluación Integral de Sostenibilidad
            </div>

            <div class="header-company">
                ACUAMAR S.A.
            </div>
            """,
            unsafe_allow_html=True
        )

    # ------------------------------------------------------

    # FECHA

    # ------------------------------------------------------

    with col_fecha:

        st.markdown(
            f"""
            <div class="header-date">

            <b>{fecha}</b>

            <br>

            Versión 1.0

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="header-badge">

        🌍 Environmental • Social • Governance

        </div>

        <hr>
        """,
        unsafe_allow_html=True
    )
