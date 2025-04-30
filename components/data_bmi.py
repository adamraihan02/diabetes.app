import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan statistik deskriptif dan visualisasi distribusi
def run_data_bmi():
    st.title("Data BMI")
    
    # Cek apakah file CSV sudah ada
    if os.path.exists("data/data_bmi.csv"):
        # Baca data dari CSV
        df = pd.read_csv("data/data_bmi.csv")
        
        # Tampilkan data dalam bentuk tabel
        st.dataframe(df)
        
        # Checkbox untuk menampilkan statistik deskriptif
        if st.checkbox("Tampilkan Statistik Deskriptif"):
            st.write(df.describe())

        # Checkbox untuk menampilkan visualisasi distribusi
        if st.checkbox("Tampilkan Visualisasi Distribusi BMI"):
            plt.figure(figsize=(10, 6))
            sns.histplot(df['BMI'], kde=True, bins=20)
            plt.title('Distribusi BMI')
            plt.xlabel('BMI')
            plt.ylabel('Frekuensi')
            st.pyplot(plt.gcf())

    else:
        st.write("Belum ada data BMI yang tersimpan.")
