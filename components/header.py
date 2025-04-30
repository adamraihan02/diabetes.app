import streamlit as st

def header():
    st.markdown(
        """
        <style>
        .sticky-header {
            position: -webkit-sticky;
            position: sticky;
            top: 0;
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            z-index: 100;
            display: flex;
            align-items: center;
        }
        .sticky-header img {
            margin-right: 10px;
            width: 50px;
            height: 50px;
        }
        .sticky-header h1 {
            font-size: 24px;
            font-weight: bold;
        }
        </style>

        <div class="sticky-header">
            <img src="https://storage.googleapis.com/a1aa/image/ihHHKeqSpQVgVKqTDa7rj1n3gMEUBH9xugnIMJetbDyfiPSoA.jpg" alt="Ampire Logo">
            <h1>Aplikasi GlycoVision</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
