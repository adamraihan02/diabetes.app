import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Fungsi utama untuk halaman Data BMI
def run_data_bmi():
    st.title("📊 Data BMI yang Tersimpan")

    # Mengakses spreadsheet untuk menampilkan data BMI
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["connections"]["gsheets"], scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("data_glyco")
        sheet = spreadsheet.sheet1
        data = sheet.get_all_records()

        if data:
            df = pd.DataFrame(data)

            st.subheader("📋 Tabel Data BMI")
            st.dataframe(df)

            st.markdown(f"**Jumlah Data:** {len(df)}")

            # Statistik deskriptif
            if st.checkbox("Tampilkan Statistik Deskriptif"):
                st.subheader("Statistik Deskriptif")
                st.write(df.describe())

            # Visualisasi distribusi BMI
            if st.checkbox("Tampilkan Visualisasi Distribusi BMI"):
                st.subheader("Distribusi BMI")
                plt.figure(figsize=(10, 6))
                sns.histplot(df['BMI'], kde=True, bins=20, color="skyblue")
                plt.title("Distribusi Nilai BMI")
                plt.xlabel("BMI")
                plt.ylabel("Frekuensi")
                st.pyplot(plt.gcf())

            # Visualisasi kategori BMI
            if st.checkbox("Tampilkan Distribusi Kategori BMI"):
                st.subheader("Distribusi Kategori BMI")
                kategori_counts = df['Kategori'].value_counts()

                fig, ax = plt.subplots(figsize=(8, 5))
                sns.barplot(x=kategori_counts.index, y=kategori_counts.values, palette="Set2", ax=ax)
                ax.set_ylabel("Jumlah")
                ax.set_xlabel("Kategori BMI")
                ax.set_title("Jumlah Data per Kategori BMI")
                st.pyplot(fig)

        else:
            st.warning("⚠️ Belum ada data BMI yang tersimpan.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat mengambil data dari Google Sheets: {e}")
