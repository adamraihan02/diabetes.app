import streamlit as st
import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Fungsi untuk mengkategorikan BMI dan rekomendasi berat badan
def kategori_bmi(bmi, height, weight):
    if bmi < 18.5:
        normal_weight_min = 18.5 * (height / 100) ** 2
        gain_weight = normal_weight_min - weight
        return "Underweight", gain_weight, "naik"
    elif 18.5 <= bmi <= 24.9:
        return "Normal", 0, ""
    elif 25 <= bmi <= 29.9:
        normal_weight_max = 24.9 * (height / 100) ** 2
        lose_weight = weight - normal_weight_max
        return "Overweight", lose_weight, "turun"
    elif 30 <= bmi <= 34.9:
        normal_weight_max = 24.9 * (height / 100) ** 2
        lose_weight = weight - normal_weight_max
        return "Obesity", lose_weight, "turun"
    else:
        normal_weight_max = 24.9 * (height / 100) ** 2
        lose_weight = weight - normal_weight_max
        return "Very obese", lose_weight, "turun"

# Fungsi untuk menampilkan hasil BMI
def view_result(bmi, category, weight_change, action):
    st.write(f"Kategori BMI Anda: **{category}**")

    if category == "Normal":
        st.success("BMI Anda sudah berada dalam kategori normal.")
    else:
        st.warning(f"Untuk mencapai kategori normal, Anda perlu {action} berat badan sebanyak {weight_change:.2f} kg.")

    # Gambar sesuai kategori
    image_path = ""
    if category == "Underweight":
        image_path = "images/under.jpeg"
    elif category == "Normal":
        image_path = "images/normal.jpeg"
    elif category == "Overweight":
        image_path = "images/over.jpeg"
    elif category == "Obesity":
        image_path = "images/obes.jpeg"

    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=f"Kategori BMI: {category}", width=200)
    else:
        st.info("Gambar tidak tersedia untuk kategori ini.")

# Fungsi menyimpan data ke Google Sheets
def save_data(name, weight, height, bmi, category):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    # Menggunakan kredensial yang diatur di secrets.toml
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["connections"]["gsheets"], scope)
    client = gspread.authorize(creds)

    # Mengakses spreadsheet yang sudah ada
    spreadsheet = client.open("data_glyco")
    sheet = spreadsheet.sheet1

    row = [name, weight, height, f"{bmi:.1f}", category]
    sheet.append_row(row)

# Fungsi utama halaman BMI
def run():
    st.image('images/indeks BMI.jpeg', caption='INDEKS BMI', width=600)
    st.title("🧮 Kalkulator BMI")

    if os.path.exists("styles.css"):
        with open("styles.css") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    name_input = st.text_input("Masukkan nama Anda", placeholder="Nama")
    weight_input = st.text_input("Masukkan berat badan Anda (kg):", placeholder="0")
    height_input = st.text_input("Masukkan tinggi badan Anda (cm):", placeholder="0")

    if st.button("Cek BMI"):
        try:
            weight = float(weight_input)
            height = float(height_input)

            if weight > 0 and height > 0 and name_input.strip():
                bmi = weight / ((height / 100) ** 2)
                st.write(f"BMI Anda adalah: **{bmi:.2f}**")

                kategori, weight_change, action = kategori_bmi(bmi, height, weight)

                view_result(bmi, kategori, weight_change, action)
                save_data(name_input, weight, height, bmi, kategori)
            else:
                st.warning("Semua input harus diisi dan bernilai lebih dari 0.")
        except ValueError:
            st.error("Masukkan berat dan tinggi badan dalam format angka.")
