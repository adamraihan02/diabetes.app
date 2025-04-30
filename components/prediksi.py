import streamlit as st
import pickle
import pandas as pd
import os

# Membaca model dan scaler
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    scaler = pickle.load(open('scaler.sav', 'rb'))  # Pastikan scaler juga disimpan saat training
except FileNotFoundError:
    st.error("Model atau scaler tidak ditemukan!")

# Fungsi untuk menyimpan data prediksi ke CSV
def save_data(data):
    filename = "data_pasien_perempuan.csv"
    df = pd.DataFrame([data])

    # Jika file belum ada, buat file baru
    if not os.path.exists(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

def run():
    st.title('Prediksi Diabetes')

    # Memuat CSS dari file
    if os.path.exists("styles.css"):
        with open("styles.css") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Form input
    with st.form(key='input_form'):
        pregnancies_input = st.text_input('Masukkan jumlah kehamilan (Pregnancies):', placeholder="0")
        glucose_input = st.text_input('Masukkan kadar glukosa (Glucose):', placeholder="0")
        bmi_input = st.text_input('Masukkan BMI:', placeholder="0.0")
        dpf_input = st.text_input('Masukkan Diabetes Pedigree Function:', placeholder="0.0")
        age_input = st.text_input('Masukkan usia (Age):', placeholder="0")

        # Tombol untuk melakukan prediksi
        submit_button = st.form_submit_button(label='Prediksi')

        if submit_button:
            try:
                # Konversi input menjadi float
                input_data = [
                    int(pregnancies_input),
                    float(glucose_input),
                    float(bmi_input),
                    float(dpf_input),
                    int(age_input)
                ]

                # Scaling input data
                scaled_input = scaler.transform([input_data])

                # Prediksi dengan model
                diab_prediction = diabetes_model.predict(scaled_input)

                # Menentukan diagnosis berdasarkan prediksi
                diab_diagnosis = 'Pasien terkena Diabetes' if diab_prediction[0] == 1 else 'Pasien tidak terkena Diabetes'

                # Menampilkan hasil prediksi
                st.success(diab_diagnosis)

                # Simpan data ke CSV
                data = {
                    "Pregnancies": input_data[0],
                    "Glucose": input_data[1],
                    "BMI": input_data[2],
                    "DiabetesPedigreeFunction": input_data[3],
                    "Age": input_data[4],
                    "Diagnosis": diab_diagnosis
                }
                save_data(data)

            except ValueError:
                st.error("Silakan masukkan semua nilai input dengan format yang benar (numerik).")
            except Exception as e:
                st.error(f"Terjadi kesalahan dalam prediksi: {str(e)}")

    # Penjelasan tabel
    st.markdown('<h2 class="custom-subtitle">Penjelasan Tabel:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Pregnancies:</strong> Jumlah kehamilan yang pernah dialami.</li>'
                '<li><p class="custom-text"><strong>Glucose:</strong> Tingkat glukosa dalam darah (setelah tes beban glukosa 2 jam).</li>'
                '<li><p class="custom-text"><strong>BMI:</strong> Indeks Massa Tubuh (ukuran berat badan relatif terhadap tinggi badan).</li>'
                '<li><p class="custom-text"><strong>DiabetesPedigreeFunction:</strong> Ukuran risiko genetik diabetes berdasarkan riwayat keluarga.</li>'
                '<li><p class="custom-text"><strong>Age:</strong> Usia pasien.</li>'
                '</ul>', unsafe_allow_html=True)

if __name__ == "__main__":
    run()
