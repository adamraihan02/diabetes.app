import streamlit as st
from streamlit_option_menu import option_menu


def sidebar():
    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Dashboard", "Kalkulator BMI", "Prediksi", "Lokasi Rumah Sakit", "Data BMI", "Data Diabetes"],
            icons = ["house", "calculator", "graph-up-arrow", "hospital", "table", "map"],
            menu_icon="grid",
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#f8f9fa"},
                "icon": {"color": "#007bff", "font-size": "18px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#007bff", "color": "white"},
            },
        )
    return selected
