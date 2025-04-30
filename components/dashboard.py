import streamlit as st

def page_description():
    # CSS untuk mempercantik tampilan
    st.markdown("""
        <style>
            .title-container {
                font-size: 40px;
                font-weight: 800;
                color: #007BFF;
                line-height: 1.2;
                margin-bottom: 10px;
            }
            .custom-title {
              color: #007BFF; /* Warna biru */
              font-size: 35px;
              font-weight: bold;
              margin-bottom: 15px;
            }
            .description-container {
                font-size: 18px;
                color: #333;
                margin-bottom: 20px;
            }
            .info-card {
                background-color: #fdf3f3;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
                width: 160px;
                margin-top: 20px;
            }
            .info-card h3 {
                margin: 0;
                font-size: 28px;
                color: #B80000;
            }
            .info-card p {
                margin: 0;
                font-size: 14px;
                color: #555;
            }
            .btn-custom {
                padding: 0.6em 1.4em;
                border-radius: 8px;
                border: none;
                background-color: #B80000;
                color: white;
                font-weight: bold;
                font-size: 16px;
                margin-right: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Tampilan dua kolom
    col1, col2 = st.columns([2, 1])

    # Konten Kiri
    with col1:
        st.markdown('<div class="title-container">Deteksi Risiko Diabetes</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="description-container">Aplikasi ini menggunakan teknologi AI untuk membantu Anda mendeteksi risiko diabetes berdasarkan faktor kesehatan dan gaya hidup Anda. Dapatkan hasil prediksi instan hanya dengan beberapa input sederhana.</div>',
            unsafe_allow_html=True,
        )
        

        # Keunggulan
        st.markdown("✅ Teknologi AI Terkini &nbsp;&nbsp;&nbsp; ✅ Hasil Cepat &nbsp;&nbsp;&nbsp; ✅ Tampilan Interaktif")

    # Konten Kanan
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=250)

    st.markdown('<h1 class="custom-title">Diabetes atau gula</h1>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Diabetes melitus, atau yang lebih dikenal sebagai penyakit gula, adalah suatu kondisi kronis di mana tubuh tidak mampu mengatur kadar gula darah dengan baik. Hal ini terjadi karena tubuh tidak menghasilkan cukup insulin, hormon yang mengatur penggunaan gula darah, atau karena sel-sel tubuh menjadi resisten terhadap insulin. Akibatnya, gula darah menumpuk dalam darah dan dapat merusak berbagai organ tubuh seperti jantung, ginjal, saraf, dan mata. Diabetes dapat dibagi menjadi beberapa jenis, yaitu diabetes tipe 1, diabetes tipe 2, dan diabetes gestasional. Diabetes tipe 1 disebabkan oleh kerusakan sel-sel penghasil insulin di pankreas, sedangkan diabetes tipe 2 lebih sering disebabkan oleh kombinasi faktor genetik dan gaya hidup yang tidak sehat. Diabetes gestasional terjadi pada wanita hamil dan biasanya hilang setelah melahirkan.</p>', unsafe_allow_html=True)


    st.markdown('<h1 class="custom-title"> Beberapa teori yang menjelaskan mengapa diabetes lebih sering terjadi pada wanita, antara lain:</h1>', unsafe_allow_html=True)
    st.markdown("""
    
    **1. Hormon:**  
    Fluktuasi hormon selama siklus menstruasi, kehamilan, dan menopause dapat mempengaruhi sensitivitas tubuh terhadap insulin. Perubahan hormon ini dapat meningkatkan risiko resistensi insulin dan diabetes tipe 2.
    
    **2. Genetik:**  
    Beberapa gen tertentu dapat meningkatkan risiko diabetes pada wanita. Gen-gen ini dapat mempengaruhi metabolisme glukosa dan produksi insulin.
    
    **3. Gaya hidup:**  
    Faktor gaya hidup seperti pola makan yang tidak sehat, kurang aktivitas fisik, dan stres juga dapat meningkatkan risiko diabetes pada wanita.
    
    **4. Obat-obatan:**  
    Beberapa jenis obat, seperti kortikosteroid dan kontrasepsi oral, dapat meningkatkan kadar gula darah dan meningkatkan risiko diabetes.
    
    **5. Sindrom Ovarium Polikistik (SOP):**  
    Wanita dengan SOP memiliki risiko lebih tinggi terkena diabetes tipe 2 karena gangguan metabolisme glukosa dan insulin.
    """)

    st.markdown('<h1 class="custom-title"> Peran Nutrisi dan Olahraga dalam Mengelola Diabetes pada Wanita:</h1>', unsafe_allow_html=True)
    st.markdown("""
    Nutrisi dan olahraga adalah dua pilar utama dalam pengelolaan diabetes, baik pada pria maupun wanita. Keduanya memiliki peran yang sangat penting dalam membantu menjaga kadar gula darah tetap stabil, mengurangi risiko komplikasi, dan meningkatkan kualitas hidup penderita diabetes.

    ### Peran Nutrisi
    - **Mengontrol asupan karbohidrat:**  
      Karbohidrat adalah sumber utama glukosa dalam tubuh. Oleh karena itu, mengontrol asupan karbohidrat sangat penting untuk menjaga kadar gula darah tetap stabil.
    - **Memilih sumber protein yang baik:**  
      Protein membantu menjaga rasa kenyang lebih lama, sehingga mengurangi keinginan untuk ngemil dan membantu mengontrol berat badan.
    - **Mengkonsumsi lemak sehat:**  
      Lemak sehat seperti yang terdapat pada minyak zaitun, alpukat, dan kacang-kacangan dapat membantu meningkatkan sensitivitas insulin.
    - **Membatasi konsumsi gula tambahan dan makanan olahan:**  
      Makanan dan minuman manis mengandung banyak gula tambahan yang dapat meningkatkan kadar gula darah dengan cepat.
    - **Mengonsumsi serat:**  
      Serat membantu memperlambat penyerapan gula ke dalam darah, sehingga membantu menjaga kadar gula darah tetap stabil.

    ### Peran Olahraga
    - **Meningkatkan sensitivitas insulin:**  
      Olahraga secara teratur membantu sel-sel tubuh menjadi lebih sensitif terhadap insulin, sehingga gula darah dapat masuk ke dalam sel dengan lebih mudah.
    - **Membantu membakar glukosa:**  
      Olahraga membakar glukosa sebagai energi, sehingga membantu menurunkan kadar gula darah.
    - **Membantu mengontrol berat badan:**  
      Olahraga dapat membantu menurunkan berat badan atau menjaga berat badan ideal, yang sangat penting bagi penderita diabetes, terutama tipe 2.
    - **Meningkatkan kesehatan jantung dan pembuluh darah:**  
      Diabetes meningkatkan risiko penyakit jantung dan pembuluh darah. Olahraga secara teratur dapat membantu menurunkan risiko komplikasi ini.

    ### Nutrisi dan Olahraga Khusus untuk Wanita
    - **Kehamilan:**  
      Wanita hamil dengan diabetes gestasional perlu memperhatikan pola makan dan olahraga yang ketat untuk menjaga kadar gula darah tetap stabil dan mencegah komplikasi pada ibu dan bayi.
    - **Menopause:**  
      Perubahan hormon selama menopause dapat mempengaruhi metabolisme glukosa. Oleh karena itu, wanita menopause dengan diabetes perlu menyesuaikan pola makan dan olahraga mereka.
    - **Sindrom Ovarium Polikistik (SOP):**  
      Wanita dengan SOP seringkali memiliki resistensi insulin dan berisiko tinggi terkena diabetes tipe 2. Pola makan yang sehat dan olahraga teratur dapat membantu mengelola kondisi ini.
    """)


    st.markdown('<h2 class="custom-subtitle">Jenis-jenis Diabetes:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Diabetes Tipe 1:</strong> Terjadi ketika tubuh tidak menghasilkan insulin sama sekali. Insulin adalah hormon yang berperan dalam membantu glukosa masuk ke dalam sel.</li>'
                '<li><p class="custom-text"><strong>Diabetes Tipe 2:</strong> Jenis yang paling umum, terjadi ketika tubuh tidak dapat menggunakan insulin dengan baik atau tidak menghasilkan cukup insulin.</li>'
                '<li><p class="custom-text"><strong>Gestational Diabetes:</strong> Diabetes yang terjadi selama kehamilan.</li>'
                '</ul>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="custom-subtitle">Gejala Diabetes yang Perlu Diwaspadai:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Sering buang air kecil:</strong> Terutama pada malam hari.</li>'
                '<li><p class="custom-text"><strong>Sering merasa haus:</strong> Meskipun banyak minum.</li>'
                '<li><p class="custom-text"><strong>Rasa lapar yang berlebihan: </strong> Meskipun baru saja makan.</li>'
                '<li><p class="custom-text"><strong>Penurunan berat badan tanpa sebab yang jelas. </strong></li>'
                '<li><p class="custom-text"><strong>Kelelahan. </strong> </li>'
                '<li><p class="custom-text"><strong>Pandangan kabur. </strong></li>'
                '<li><p class="custom-text"><strong>Luka yang sulit sembuh. </strong></li>'
                '<li><p class="custom-text"><strong>Kesemutan atau mati rasa pada tangan dan kaki. </strong> </li>'
                '</ul>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="custom-subtitle">Komplikasi Diabetes:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Penyakit jantung:</strong> Serangan jantung dan stroke.</li>'
                '<li><p class="custom-text"><strong>Kerusakan ginjal:</strong> Hingga memerlukan dialisis.</li>'
                '<li><p class="custom-text"><strong>Kerusakan saraf:</strong> Neuropati.</li>'
                '<li><p class="custom-text"><strong>Masalah pada mata: Katarak dan retinopati diabetik.</strong></li>'
                '<li><p class="custom-text"><strong>Gangguan pada kaki: Ulkus diabetik dan amputasi.</strong> </li>'
                '</ul>', unsafe_allow_html=True)

    st.markdown('<h2 class="custom-title">Diabetes tipe 1 dan diabetes tipe 2 adalah dua jenis diabetes yang paling umum, namun keduanya memiliki penyebab dan mekanisme yang berbeda.</h2>', unsafe_allow_html=True)
    st.markdown('<h2 class="custom-subtitle">Diabetes tipe 1:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Penyebab:</strong> Sistem kekebalan tubuh secara keliru menyerang sel-sel penghasil insulin di pankreas. Akibatnya, tubuh tidak dapat memproduksi insulin sama sekali.</li>'
                '<li><p class="custom-text"><strong>Umumnya terjadi pada:</strong> Anak-anak dan remaja, meskipun bisa terjadi pada orang dewasa.</li>'
                '<li><p class="custom-text"><strong>Gejala:</strong> Muncul secara tiba-tiba dan biasanya parah, seperti sering buang air kecil, rasa haus yang berlebihan, penurunan berat badan drastis, kelelahan, dan penglihatan kabur.</li>'
                '<li><p class="custom-text"><strong>Pengobatan: </strong> Injeksi insulin seumur hidup untuk menggantikan insulin yang tidak diproduksi oleh tubuh.</li>'
                '</ul>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="custom-subtitle">Diabetes tipe 2:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Penyebab:</strong> Tubuh tidak dapat menggunakan insulin secara efektif (resistensi insulin) atau pankreas tidak memproduksi cukup insulin.</li>'
                '<li><p class="custom-text"><strong>Umumnya terjadi pada:</strong>  Orang dewasa, terutama yang kelebihan berat badan, kurang aktif, dan memiliki riwayat keluarga diabetes.</li>'
                '<li><p class="custom-text"><strong>Gejala:</strong>Seringkali tidak menunjukkan gejala yang jelas pada tahap awal, atau gejalanya lebih ringan dibandingkan diabetes tipe 1. Gejala umum termasuk sering buang air kecil, rasa haus, mudah lelah, dan luka yang sulit sembuh.</li>'
                '<li><p class="custom-text"><strong>Pengobatan: </strong> Kombinasi dari perubahan gaya hidup (diet sehat, olahraga teratur), obat-obatan oral, dan dalam beberapa kasus, injeksi insulin.</li>'
                '</ul>', unsafe_allow_html=True)
    st.image('images/perbedaan diabetes 1 dan 2.jpeg',  caption='perbedaan diabetes 1 dan 2 by:hallosehat', width=500)

    st.markdown('<h2 class="custom-subtitle">Hidup dengan Diabetes:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Tantangan:</strong> Mengelola kadar gula darah setiap hari, menjaga pola makan, dan mengatasi stres.</li>'
                '<li><p class="custom-text"><strong>Dukungan:</strong>  Pentingnya dukungan keluarga, teman, dan komunitas penderita diabetes.</li>'
                '<li><p class="custom-text"><strong>Teknologi:</strong> Perkembangan teknologi seperti pompa insulin, sensor glukosa kontinu, dan aplikasi mobile memudahkan pengelolaan diabetes.</li>'
                '</ul>', unsafe_allow_html=True)
    # Pengaturan gambar bersampingan dengan menggunakan kolom
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/pompa insulin.jpeg', caption='pompa insulin by:hallosehat', use_column_width=True)

    with col2:
        st.image('images/sensor glukosa.jpeg', caption='sensor glukosa darah', use_column_width=True)

    st.markdown('<h2 class="custom-subtitle">Apa perbedaan antara hipoglikemia dan hiperglikemia?</h2>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text"><strong>Hipoglikemia:</strong> Kondisi di mana kadar gula darah terlalu rendah. Ini sering disebut dengan gula darah rendah. Gejalanya bisa berupa:</p>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li>Kelemahan</li>'
                '<li>Pusing</li>'
                '<li>Berkeringat</li>'
                '<li>Lapar</li>'
                '<li>Jantung Berdebar</li>'
                '<li>Kesulitan Berkonsentrasi</li>'
                '<li>Perubahan perilaku (iritabilitas, kebingungan)</li>'
                '<li>Kehilangan kesadaran (dalam kasus yang parah)</li>'
                '</ul>', unsafe_allow_html=True)
    
    st.markdown('<p class="custom-text"><strong>Hiperglikemia:</strong> Kondisi di mana kadar gula darah terlalu tinggi. Ini sering disebut dengan gula darah tinggi. Gejalanya bisa berupa:</p>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li>Sering buang air kecil</li>'
                '<li>Rasa haus yang berlebihan</li>'
                '<li>Kelelahan</li>'
                '<li>Penglihatan Kabur</li>'
                '<li>Luka yang sulit sembuh</li>'
                '<li>Nafar berbau buah (dalam kasus ketoasidosis diabetik)</li>'
                '</ul>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="custom-subtitle">Bagaimana cara memilih makanan yang tepat untuk penderita diabetes?</h2>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text"> Memilih makanan yang tepat sangat penting bagi penderita diabetes untuk menjaga kadar gula darah tetap stabil. Berikut beberapa tips:</p>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Prioritaskan karbohidrat kompleks: :</strong>  Pilihlah sumber karbohidrat kompleks seperti nasi merah, roti gandum utuh, oatmeal, dan sayuran bertepung. Karbohidrat kompleks dicerna lebih lambat, sehingga tidak menyebabkan lonjakan gula darah yang drastis.</li>'
                '<li><p class="custom-text"><strong>Batasi konsumsi gula tambahan:</strong>  Pentingnya dukungan keluarga, teman, dan komunitas penderita diabetes.</li>'
                '<li><p class="custom-text"><strong>Pilih protein tanpa lemak:</strong> Daging tanpa lemak, ikan, telur, dan kacang-kacangan adalah sumber protein yang baik. Protein membantu memperlambat penyerapan karbohidrat.</li>'
                '<li><p class="custom-text"><strong>Konsumsi serat yang cukup:</strong> Serat membantu memperlambat penyerapan gula darah. Sumber serat yang baik adalah buah-buahan, sayuran, dan biji-bijian.</li>'
                '<li><p class="custom-text"><strong>Perhatikan ukuran porsi:</strong> Meskipun makanan sehat, tetap penting untuk memperhatikan ukuran porsi agar tidak berlebihan.</li>'
                '<li><p class="custom-text"><strong>Baca label nutrisi:</strong> Perhatikan kandungan karbohidrat, gula, dan lemak dalam setiap makanan.</li>'
                '</ul>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="custom-subtitle">Contoh makanan yang baik untuk penderita diabetes:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Buah-buahan:</strong> Apel, pir, beri-berian, jeruk</li>'
                '<li><p class="custom-text"><strong>Sayuran:</strong> Brokoli, bayam, kubis, wortel</li>'
                '<li><p class="custom-text"><strong>Biji-bijian:</strong> Nasi merah, roti gandum utuh, quinoa</li>'
                '<li><p class="custom-text"><strong>Protein:</strong> Daging tanpa lemak, ikan, telur, kacang-kacangan, tahu</li>'
                '<li><p class="custom-text"><strong>Susu:</strong> Susu rendah lemak atau skim, yogurt rendah lemak</li>'
                '</ul>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="custom-subtitle">Contoh makanan yang sebaiknya dihindari:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li><p class="custom-text"><strong>Makanan manis:</strong> Permen, cokelat, kue, minuman bersoda</li>'
                '<li><p class="custom-text"><strong>Makanan olahan:</strong> Keripik, makanan cepat saji</li>'
                '<li><p class="custom-text"><strong>Minuman manis:</strong> Jus buah kemasan, minuman bersoda</li>'
                '<li><p class="custom-text"><strong>Protein:</strong> Daging tanpa lemak, ikan, telur, kacang-kacangan, tahu</li>'
                '<li><p class="custom-text"><strong>Lemak jenuh dan trans:</strong> Daging berlemak, mentega, margarin</li>'
                '</ul>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text"><strong>Penting:</strong> Setiap orang dengan diabetes memiliki kebutuhan yang berbeda. Disarankan untuk berkonsultasi dengan ahli gizi atau dokter untuk membuat rencana makan yang sesuai dengan kondisi kesehatan Anda.</p>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="custom-subtitle">Efektivitas Olahraga dalam Mengontrol Gula Darah pada Penderita Diabetes</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li>Meningkatkan sensitivitas insulin: Olahraga membantu sel-sel tubuh menjadi lebih responsif terhadap insulin, sehingga glukosa lebih mudah masuk ke dalam sel dan kadar gula darah menurun.</li>'
                '<li>Membantu tubuh menggunakan glukosa sebagai energi: Saat berolahraga, otot-otot menggunakan glukosa sebagai bahan bakar, sehingga kadar gula darah juga ikut turun.</li>'
                '<li>Membantu menurunkan berat badan: Obesitas adalah salah satu faktor risiko utama diabetes tipe 2. Dengan berolahraga, berat badan dapat terkontrol dan sensitivitas insulin pun meningkat.</li>'
                '</ul>', unsafe_allow_html=True)

    st.markdown('<h2 class="custom-subtitle">Jenis Olahraga yang Dianjurkan:</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="custom-list">'
                '<li>Olahraga aerobik: Jalan cepat, berlari, bersepeda, berenang.</li>'
                '<li>Olahraga kekuatan: Angkat beban ringan, latihan resistance band.</li>'
                '</ul>', unsafe_allow_html=True)

    st.markdown('<p class="custom-text"><strong>Penting:</strong> Sebelum memulai program olahraga, sebaiknya konsultasikan dengan dokter untuk mendapatkan anjuran yang sesuai dengan kondisi kesehatan masing-masing.</p>', unsafe_allow_html=True)
    # Menambahkan gambar
    st.image('images/tips diabet.png',  caption='Tips Mudah Mencegah Diabetes', width=300)
