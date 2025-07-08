import streamlit as st
from auth import login, logout_button

from components.sidebar import sidebar
from components.dashboard import page_description
from components.bmi import run as run_bmi
from components.prediksi import run as run_prediksi
from components.rumahsakit import run as run_rumahsakit
from components.data_bmi import run_data_bmi
from components.data_diabetes import run as run_data_diabetes

def main():
    # Sidebar dengan logo dan logout
    with st.sidebar:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("images/logo glyco.png", width=100)
        with col2:
            st.markdown("<h3 style='margin-top: 30px; margin-left:30px;'>GlycoVision APP</h3>", unsafe_allow_html=True)

        # Tampilkan tombol logout jika sudah login
        logout_button()

    # Tampilkan navigasi sidebar (tetap semua menu tampil)
    selected_page = sidebar()

    # Routing ke halaman
    if selected_page == "Edukasi Diabetes":
        page_description()
    elif selected_page == "Kalkulator BMI":
        run_bmi()
    elif selected_page == "Prediksi":
        run_prediksi()
    elif selected_page == "Lokasi Rumah Sakit":
        run_rumahsakit()
    elif selected_page == "Data BMI":
        if st.session_state.get("logged_in"):
            run_data_bmi()
        else:
            st.warning("🔒 Halaman ini hanya bisa diakses setelah login.")
            login()
    elif selected_page == "Data Diabetes":
        if st.session_state.get("logged_in"):
            run_data_diabetes()
        else:
            st.warning("🔒 Halaman ini hanya bisa diakses setelah login.")
            login()
    else:
        st.warning("Halaman tidak ditemukan.")

if __name__ == "__main__":
    main()
