import streamlit as st
import pandas as pd
import os

# Fungsi untuk halaman menampilkan data diabetes
def run():
    st.title("Data Diabetes")

    # Cek apakah file CSV sudah ada
    if os.path.exists("data/data_diabetes.csv"):
        # Baca data dari CSV
        df = pd.read_csv("data/data_diabetes.csv")
        st.dataframe(df)  # Tampilkan data dalam bentuk tabel

        # Menambahkan opsi untuk menampilkan ringkasan statistik
        if st.checkbox("Tampilkan Ringkasan Statistik"):
            st.write(df.describe())  # Menampilkan ringkasan statistik dasar

    else:
        st.write("Belum ada data diabetes yang tersimpan.")
