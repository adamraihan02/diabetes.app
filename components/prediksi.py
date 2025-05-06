import streamlit as st
import pickle
import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Membaca model dan scaler
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    scaler = pickle.load(open('scaler.sav', 'rb'))
except FileNotFoundError:
    st.error("Model atau scaler tidak ditemukan!")

# Fungsi untuk menyimpan data ke Google Sheets
def save_data_to_sheets(data):
    # Autentikasi dan koneksi ke Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["connections"]["gsheets"], scope)
    client = gspread.authorize(creds)
    
    # Akses spreadsheet dan sheet untuk data pasien
    spreadsheet = client.open_by_url(st.secrets["connections"]["gsheets"]["spreadsheet"])
    sheet = spreadsheet.get_worksheet(1)  # Sheet kedua untuk data pasien

    try:
        # Menambahkan data ke sheet
        sheet.append_row(data)
        return True
    except Exception as e:
        st.error(f"Gagal menyimpan data pasien ke Google Sheets: {str(e)}")
        return False

# Fungsi utama
def run():
    st.title("🩺 Deteksi Penyakit Diabetes")

    if os.path.exists("styles.css"):
        with open("styles.css") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with st.form(key='input_form'):
        pregnancies_input = st.text_input('Jumlah kehamilan (Pregnancies):', placeholder="0")
        glucose_input = st.text_input('Kadar glukosa (Glucose):', placeholder="0")
        bmi_input = st.text_input('BMI:', placeholder="0.0")
        dpf_input = st.text_input('Diabetes Pedigree Function:', placeholder="0.0")
        age_input = st.text_input('Usia (Age):', placeholder="0")

        submit_button = st.form_submit_button(label='Prediksi')

        if submit_button:
            if not all([pregnancies_input, glucose_input, bmi_input, dpf_input, age_input]):
                st.warning("⚠️ Semua kolom harus diisi.")
            else:
                try:
                    # Mengonversi input
                    input_data = [
                        int(pregnancies_input),
                        float(glucose_input),
                        float(bmi_input),
                        float(dpf_input),
                        int(age_input)
                    ]

                    # Skalakan data
                    scaled_input = scaler.transform([input_data])

                    # Prediksi
                    diab_prediction = diabetes_model.predict(scaled_input)
                    diab_diagnosis = 'Pasien terkena Diabetes' if diab_prediction[0] == 1 else 'Pasien tidak terkena Diabetes'

                    # Tampilkan hasil prediksi
                    st.success(f"✅ Hasil Prediksi: {diab_diagnosis}")

                    # Data yang akan disimpan ke Google Sheets
                    data = [
                        input_data[0],  # Pregnancies
                        input_data[1],  # Glucose
                        input_data[2],  # BMI
                        input_data[3],  # DiabetesPedigreeFunction
                        input_data[4],  # Age
                        diab_diagnosis  # Diagnosis
                    ]

                    # Coba simpan data dan beri notifikasi
                    if save_data_to_sheets(data):
                        st.info("📁 Data pasien berhasil disimpan ke Google Sheets.")
                    else:
                        st.warning("❌ Data pasien tidak berhasil disimpan.")

                except ValueError:
                    st.error("❌ Masukkan data dalam format numerik yang benar.")
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {str(e)}")

    # Penjelasan tabel fitur
    st.markdown('<h3 class="custom-subtitle">Penjelasan Input:</h3>', unsafe_allow_html=True)
    st.markdown('''<ul class="custom-list">
        <li><strong>Pregnancies:</strong> Jumlah kehamilan.</li>
        <li><strong>Glucose:</strong> Kadar glukosa darah (mg/dL).</li>
        <li><strong>BMI:</strong> Indeks massa tubuh.</li>
        <li><strong>DiabetesPedigreeFunction:</strong> Riwayat genetik diabetes dalam keluarga.</li>
        <li><strong>Age:</strong> Usia pasien (tahun).</li>
    </ul>''', unsafe_allow_html=True)

if __name__ == "__main__":
    run()
