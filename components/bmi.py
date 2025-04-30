import streamlit as st
import pandas as pd  # Tambahkan ini untuk mengimpor pandas
import os

# Fungsi untuk mengkategorikan BMI dan memberikan rekomendasi berat badan
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

# Fungsi untuk melihat hasil
def view_result(bmi, category, weight_change, action):
    st.write(f"Kategori BMI Anda: **{category}**")

    if category == "Normal":
        st.write("BMI Anda sudah berada dalam kategori normal.")
    else:
        st.write(f"Untuk mencapai kategori normal, Anda perlu {action} berat badan sebanyak {weight_change:.2f} kg.")

    # Menampilkan gambar sesuai kategori BMI
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
        st.image(image_path, caption=f"Kategori BMI: {category}", use_column_width=600, width=250)
    else:
        st.write("Gambar tidak tersedia untuk kategori ini.")

# Fungsi untuk menyimpan data BMI ke CSV
def save_data(name, weight, height, bmi, category):
    # Format BMI menjadi 1 digit di belakang koma
    bmi = f"{bmi:.1f}"

    data = {
        "Nama": [name],  # Pastikan 'name' diambil dari input
        "Berat Badan (kg)": [weight],
        "Tinggi Badan (cm)": [height],
        "BMI": [bmi],
        "Kategori": [category]
    }
    
    df = pd.DataFrame(data)
    
    # Jika file CSV tidak ada, buat file baru
    if not os.path.exists("data_bmi.csv"):
        df.to_csv("data_bmi.csv", index=False)
    else:
        df.to_csv("data_bmi.csv", mode='a', header=False, index=False)

# Fungsi untuk halaman BMI
def run():
    # Menambahkan gambar
    st.image('images/indeks BMI.jpeg', caption='INDEKS BMI', width=600)
    st.title("Kalkulator BMI")
    
    # Input untuk nama
    name_input = st.text_input("Masukkan nama Anda", placeholder="Nama")
    # Input untuk berat badan
    weight_input = st.text_input("Masukkan berat badan Anda (kg):", placeholder="0")
    # Input untuk tinggi badan
    height_input = st.text_input("Masukkan tinggi badan Anda (cm):", placeholder="0")

    try:
        weight = float(weight_input)
        height = float(height_input)
    except ValueError:
        st.write("Silakan masukkan berat dan tinggi badan yang valid (numerik).")
        return

    if weight > 0 and height > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"BMI Anda adalah: {bmi:.2f}")

        kategori, weight_change, action = kategori_bmi(bmi, height, weight)
        
        # Melihat hasil dan rekomendasi
        if st.button("Lihat Hasil"):
            view_result(bmi, kategori, weight_change, action)
            # Tambahkan name_input dalam save_data
            save_data(name_input, weight, height, bmi, kategori)  # Menyimpan data BMI ke CSV
    else:
        st.write("Silakan masukkan berat dan tinggi badan yang valid untuk menghitung BMI.")