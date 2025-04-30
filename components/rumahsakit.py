import streamlit as st
import folium
from streamlit_folium import st_folium

def run():
    # Buat tampilan peta
    m = folium.Map(location=[-6.200000, 106.816666], zoom_start=9)

    # Data rumah sakit
    rumah_sakit = [
        {"name": "Klinik Rumah Sakit Nusantara", "latitude": -6.188054, "longitude": 106.6969604},
        {"name": "Bethsaida Hospital Diabetes Center", "latitude": -6.2548846, "longitude": 106.3174734},
        {"name": "Diabetes Connection Care Eka Hospital", "latitude": -6.2982892, "longitude": 106.6668488},
        {"name": "Gading Diabetes Center - RS Gading Pluit", "latitude": -6.166357, "longitude": 106.9129751},
        {"name": "Klinik Diabetes Terpadu", "latitude": -6.2004184, "longitude": 106.8845487},
        {"name": "Klinik Kaki Diabetes - RS Puri Cinere", "latitude": -6.3222541, "longitude": 106.7799879},
        {"name": "Klinik Rumat", "latitude": -6.4036698, "longitude": 106.7431334},
        {"name": "Klinik Diabetes Endokrin Metabolik - Klinik Utama DR. Indrajana", "latitude": -6.1659085, "longitude": 106.7590354},
        {"name": "Diabetic and Thyroid Center - Mitra Keluarga", "latitude": -6.271123, "longitude": 106.4361194},
        {"name": "Klinik AP & AP Pediatric, Growth and Diabetes Center", "latitude": -6.2284847, "longitude": 106.8254134},
    ]

    # Tambahkan marker untuk setiap rumah sakit
    for rs in rumah_sakit:
        folium.Marker(
            location=[rs["latitude"], rs["longitude"]],
            popup=f"<b>{rs['name']}</b><br>Latitude: {rs['latitude']}<br>Longitude: {rs['longitude']}",
            icon=folium.Icon(color="red", icon="plus"),
        ).add_to(m)

    # Tampilkan peta dalam Streamlit
    st.title("Peta Lokasi Rumah Sakit di Indonesia")
    st_folium(m, width=800, height=600)
