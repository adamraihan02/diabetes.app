import streamlit as st
import folium
from streamlit_folium import st_folium

def run():
    # Buat tampilan peta
    m = folium.Map(location=[-6.200000, 106.816666], zoom_start=9)

    # Data rumah sakit
    rumah_sakit = [
        {"name": "Klinik Rumah Sakit Nusantara", "latitude": -6.2396683, "longitude": 106.6953988},
        {"name": "Bethsaida Hospital Diabetes Center", "latitude": -6.2548846, "longitude": 106.622344},
        {"name": "Diabetes Connection Care Eka Hospital", "latitude": -6.2982839, "longitude": 106.6668542},
        {"name": "Gading Diabetes Center - RS Gading Pluit", "latitude": -6.1660564, "longitude": 106.9133921},
        {"name": "RUMAT Bogor - Perawatan Luka Diabetes", "latitude": -6.5295273, "longitude": 106.7074305},
        {"name": "Klinik Kaki Diabetes - RS Puri Cinere", "latitude": -6.3218587, "longitude": 106.780195},
        {"name": "RUMAT Depok - Perawatan Luka Diabetes", "latitude": -6.3216762, "longitude": 106.7003667},
        {"name": "RUMAT Cibinong - Perawatan Luka Diabetes", "latitude": -6.4726847, "longitude": 106.6989847},
        {"name": "RUMAT Cibubur - Perawatan Luka Diabetes", "latitude": -6.35199, "longitude": 106.7414191},
        {"name": "Klinik Utama DR. Indrajana", "latitude": -6.176622, "longitude": 106.8145258},
        {"name": "Rumah Sakit Mitra Keluarga Bintaro", "latitude": -6.2711177, "longitude": 106.7384151},
        {"name": "Klinik AP & AP Pediatric, Growth and Diabetes Center", "latitude": -6.2283069, "longitude": 1106.8253455},
    ]

    # Tambahkan marker untuk setiap rumah sakit
    for rs in rumah_sakit:
        # URL Google Maps
        maps_url = f"https://www.google.com/maps?q={rs['latitude']},{rs['longitude']}"
        
        # HTML Popup
        popup_html = f"""
        <b>{rs['name']}</b><br>
        Latitude: {rs['latitude']}<br>
        Longitude: {rs['longitude']}<br>
        <a href="{maps_url}" target="_blank">Buka di Google Maps</a>
        """
        
        folium.Marker(
            location=[rs["latitude"], rs["longitude"]],
            popup=folium.Popup(popup_html, max_width=250),
            icon=folium.Icon(color="red", icon="plus"),
        ).add_to(m)

    # Tampilkan peta dalam Streamlit
    st.title("Peta Lokasi Rumah Sakit di Indonesia")
    st_folium(m, width=800, height=600)
