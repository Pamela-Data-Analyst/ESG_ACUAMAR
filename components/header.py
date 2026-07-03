# ==========================================================
# HEADER CORPORATIVO
# Dashboard ESG - ACUAMAR S.A.
# ==========================================================

import streamlit as st
from pathlib import Path
from datetime import datetime
import base64


# ==========================================================
# RUTAS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

LOGO = BASE_DIR / "assets" / "logos" / "logo_acuamar.png"


# ==========================================================
# CONVERTIR IMAGEN A BASE64
# ==========================================================

def image_to_base64(image_path):

    with open(image_path, "rb") as image_file:

        encoded = base64.b64encode(image_file.read()).decode()

    return encoded


# ==========================================================
# HEADER
# ==========================================================

def mostrar_header():

    logo = image_to_base64(LOGO)

    fecha = datetime.now().strftime("%d %B %Y")

    st.markdown(
        f"""
        <style>

        .header-container{{
            background:white;
            border-radius:20px;
            padding:25px;
            box-shadow:0px 6px 20px rgba(0,0,0,.08);
            margin-bottom:25px;
        }}

        .header-grid{{
            display:flex;
            justify-content:space-between;
            align-items:center;
        }}

        .header-left{{
            display:flex;
            align-items:center;
        }}

        .logo{{
            width:90px;
            margin-right:25px;
        }}

        .titulo{{
            font-size:34px;
            font-weight:700;
            color:#0F4C81;
            margin:0;
        }}

        .subtitulo{{
            font-size:17px;
            color:#666666;
            margin-top:5px;
        }}

        .fecha{{
            font-size:15px;
            color:#888888;
            text-align:right;
        }}

        .badge{{
            display:inline-block;
            margin-top:15px;
            background:#D9F2E6;
            color:#2E8B57;
            padding:8px 18px;
            border-radius:30px;
            font-size:14px;
            font-weight:bold;
        }}

        </style>

        <div class="header-container">

            <div class="header-grid">

                <div class="header-left">

                    <img class="logo"
                    src="data:image/png;base64,{logo}">

                    <div>

                        <p class="titulo">
                        Dashboard ESG Corporativo
                        </p>

                        <p class="subtitulo">
                        Evaluación Integral de Sostenibilidad
                        <br>
                        ACUAMAR S.A.
                        </p>

                        <div class="badge">
                        🌍 Environmental • Social • Governance
                        </div>

                    </div>

                </div>

                <div class="fecha">

                    <strong>{fecha}</strong>

                    <br><br>

                    Versión 1.0

                </div>

            </div>

        </div>

        """,
        unsafe_allow_html=True,
    )
