import streamlit as st
import folium
from streamlit_folium import st_folium

def run():
    # Buat tampilan peta
    m = folium.Map(location=[-6.200000, 106.816666], zoom_start=9)

    # Data rumah sakit
    rumah_sakit = [
        {"name": "Bethsaida Hospital Diabetes Center", "latitude": -6.2548846, "longitude": 106.622344},
        {"name": "Diabetes Connection Care Eka Hospital", "latitude": -6.2989036, "longitude": 106.6699139},
        {"name": "Epitel Spesialis Luka Diabetes - Kelapa Gading Jakarta Utara", "latitude": -6.1723082, "longitude": 106.8987443},
        {"name": "RUMAT Bogor - Perawatan Luka Diabetes", "latitude": -6.58685, "longitude": 106.7835865},
        {"name": "Klinik Kaki Diabetes - RS Puri Cinere", "latitude": -6.3221637, "longitude": 106.7829289},
        {"name": "RUMAT Depok - Perawatan Luka Diabetes", "latitude":-6.403715, "longitude": 106.8191169},
        {"name": "RUMAT Cibinong - Perawatan Luka Diabetes", "latitude": -6.4726668, "longitude": 106.8432037},
        {"name": "RUMAT Nanggewer - Perawatan Luka Diabetes", "latitude": -6.5192266, "longitude": 106.835354},
        {"name": "RUMAT Cibubur - Perawatan Luka Diabetes", "latitude": -6.3519663, "longitude": 106.8855931},
        {"name": "Klinik Diabetes Endokrin Metabolik - DR. Indrajana", "latitude": -6.1124109, "longitude": 106.7530914},
        {"name": "Rumah Sakit Mitra Keluarga Bintaro", "latitude": -6.249699, "longitude": 106.6099367},
        {"name": "Klinik Diabetes mGanik Care - Spesialis Diabetes", "latitude": -6.1904549, "longitude": 106.7032886},
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

