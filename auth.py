import streamlit as st

# Daftar akun
USERS = {
    "admin": "admin123",
    "dosen": "dosen456"
}

# Fungsi login
def login():
    st.subheader("🔐 Silakan Login untuk Mengakses Halaman Ini")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success(f"Selamat datang, {username}!")
        else:
            st.error("Username atau password salah.")

# Tombol logout
def logout_button():
    if st.session_state.get('logged_in'):
        if st.button("🔓 Logout"):
            st.session_state['logged_in'] = False
            st.success("Anda telah logout.")
