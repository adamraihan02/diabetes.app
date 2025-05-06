import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def run():
    st.title("📋 Data Pasien Diabetes")

    # Autentikasi dan koneksi ke Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["connections"]["gsheets"], scope)
    client = gspread.authorize(creds)

    # Akses spreadsheet dan sheet kedua (index 1) untuk data pasien
    spreadsheet = client.open_by_url(st.secrets["connections"]["gsheets"]["spreadsheet"])
    sheet = spreadsheet.get_worksheet(1)  # Sheet ke-2

    # Ambil semua data dari sheet
    data = sheet.get_all_records()

    if data:
        df = pd.DataFrame(data)

        st.subheader("📑 Tabel Data Pasien")
        st.dataframe(df, use_container_width=True)

        st.info(f"Jumlah data tersimpan: {len(df)} pasien")

        # Ringkasan statistik
        if st.checkbox("📊 Tampilkan Ringkasan Statistik"):
            st.write(df.describe())

        # Unduh sebagai CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Unduh Data CSV",
            data=csv,
            file_name='data_pasien.csv',
            mime='text/csv'
        )
    else:
        st.warning("⚠️ Belum ada data pasien yang tersimpan.")
