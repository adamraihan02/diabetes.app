import streamlit as st
from components.sidebar import sidebar
from components.dashboard import page_description
from components.bmi import run as run_bmi
from components.prediksi import run as run_prediksi
from components.rumahsakit import run as run_rumahsakit
from components.data_bmi import run_data_bmi
from components.data_diabetes import run as run_data_diabetes

def main():
    # Tampilkan header aplikasi di sidebar
    st.sidebar.markdown(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <img src="https://storage.googleapis.com/a1aa/image/ihHHKeqSpQVgVKqTDa7rj1n3gMEUBH9xugnIMJetbDyfiPSoA.jpg" width="50" height="50" style="margin-right: 10px;">
            <h1 style="font-size: 24px; font-weight: bold;">Aplikasi GlycoVision</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Menyimpan halaman yang dipilih dalam session state
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Dashboard"  # Default page

    # Tampilkan sidebar
    selected_page = sidebar()

    # Halaman berdasarkan pemilihan
    if selected_page == "Dashboard":
        page_description()  # Tampilkan halaman dashboard
    elif selected_page == "Kalkulator BMI":
        run_bmi()
    elif selected_page == "Prediksi":
        run_prediksi()
    elif selected_page == "Lokasi Rumah Sakit":
        run_rumahsakit()
    elif selected_page == "Data BMI":
        run_data_bmi()
    elif selected_page == "Data Diabetes":
        run_data_diabetes()
    else:
        st.write("Halaman tidak ditemukan.")

if __name__ == "__main__":
    main()
