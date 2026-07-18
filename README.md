# 🎓 FAQ STMKG - Smart Assistant (Capstone Project)

Sistem berbasis _Machine Learning_ dan _Natural Language Processing_ (NLP) yang bertindak sebagai "Resepsionis Cerdas" untuk mengklasifikasikan pertanyaan (FAQ) dari taruna/i ke dalam kategori dokumen pedoman resmi secara otomatis.

Proyek ini disusun untuk memenuhi kriteria evaluasi akhir (UAS) mata kuliah Pembelajaran Mesin.

---

## 👤 Identitas Penulis

- **Nama:** Wildan Zakaria
- **NIM:** A11.2024.15768
- **mata Kuliah:** Pembelajaran Mesin
- **Kelompok:** A11.4404
- **Program Studi:** Teknik Informatika

---

## 🎯 Latar Belakang & Tujuan Proyek

Banyaknya pertanyaan berulang mengenai aturan akademik, tata tertib, dan penyusunan tugas akhir seringkali memakan waktu petugas administrasi. Proyek ini bertujuan untuk membangun model prediksi yang mampu merutekan (_routing_) pertanyaan berbasis teks ke dokumen PDF terkait dengan cepat dan akurat.

Tiga (3) kategori dokumen yang ditangani oleh sistem:

1. `Tata_Tertib_Kedisiplinan`
2. `Kurikulum_Akademik`
3. `Pedoman_Tugas_Akhir`

---

## 🏗️ Arsitektur Sistem & Alur Kerja (_Pipeline_)

Sistem ini menggunakan arsitektur _Linear Pipeline_ untuk pemrosesan teks. Alur logika program dari masukan pengguna hingga sistem memberikan jawaban adalah sebagai berikut:

`[ Input Teks ] ➔ [ Text Preprocessing & TF-IDF ] ➔ [ XGBoost Inference ] ➔ [ Prediksi Kategori & PDF Output ]`

1. **User Interface (Streamlit):** Pengguna memasukkan pertanyaan melalui antarmuka web interaktif.
2. **Text Preprocessing Engine:** Teks mentah dibersihkan (menghapus tanda baca, angka, _lowercasing_) dan dikonversi menjadi representasi numerik menggunakan **TF-IDF Vectorizer**.
3. **Machine Learning Model (Inference):** Matriks angka diproses oleh algoritma **XGBoost Classifier** untuk menghitung probabilitas dan menentukan kelas prediksi.
4. **Document Routing:** Hasil prediksi memicu sistem untuk menarik _file_ PDF pedoman resmi yang tepat dari direktori penyimpanan dan menampilkannya kepada pengguna.

---

## 🛠️ Teknologi & Library yang Digunakan

Proyek ini dikembangkan menggunakan Python dan memenuhi seluruh spesifikasi teknis yang disyaratkan:

- **Data Manipulation:** `pandas`, `numpy`
- **Visualization (Interactive & Static):** `plotly`, `matplotlib`, `seaborn`
- **Machine Learning & NLP:** `scikit-learn`, `xgboost`
- **Model Interpretation:** `lime` (Local Interpretable Model-agnostic Explanations)
- **Deployment:** `streamlit`, `pickle`

---

## ⚙️ Evaluasi Model Terbaik (XGBoost)

Model dievaluasi menggunakan _testing dataset_ dengan hasil metrik sebagai berikut:

- **Accuracy:** 82.60%
- **ROC-AUC:** 92.16% (Kemampuan pemisahan kelas yang Sangat Baik)
- **Interpretasi Model:** Menggunakan **LIME**, sistem terbukti beroperasi secara logis dalam mendeteksi kata kunci pembeda antar kategori (misalnya: kata "skripsi" dan "lembar" memicu prediksi ke kelas Tugas Akhir).

---

## 📂 Struktur Direktori (_Repository_)

Repositori ini disusun berdasarkan standar arsitektur _Software Engineering_ yang modular:

```text
capstone-project-data-mining/
├── data/
│   ├── external/          # Data referensi eksternal
│   ├── processed/         # Data hasil pembersihan (dataset_faq_stmkg.csv)
│   └── raw/               # Data mentah original
├── notebooks/
│   ├── 01_eda.ipynb       # Analisis kualitas data & visualisasi
│   ├── 02_modeling.ipynb  # Training, hyperparameter tuning, evaluasi & LIME
│   └── 03_interpretation.ipynb # Interpretasi metrik & bisnis
├── src/
│   ├── data_preprocessing.py # Script modular pemrosesan data
│   ├── train_model.py        # Script modular pelatihan model
│   ├── evaluate_model.py     # Script modular pengujian model
│   └── utils.py              # Fungsi utilitas/bantuan
├── models/
│   ├── best_model.pkl        # Model XGBoost terbaik hasil tuning
│   └── preprocessing.pkl     # Objek TF-IDF & Label Encoder
├── app/
│   ├── app.py             # Script utama aplikasi interaktif Streamlit
│   ├── assets/            # File PDF Dokumen Pedoman STMKG
│   └── pages/             # (Opsional) Halaman web tambahan
├── reports/
│   ├── final_report.pdf   # Laporan komprehensif proyek
│   └── presentation.pptx  # Slide presentasi demo
├── .gitignore             # Mengabaikan file sistem & cache Python
├── README.md              # Dokumentasi utama proyek
└── requirements.txt       # Daftar pustaka (dependencies) untuk deployment
```

🚀 Cara Instalasi & Menjalankan Aplikasi
Berikut adalah panduan untuk menjalankan proyek antarmuka Smart Assistant ini di mesin lokal:

1. Clone atau Buka Repositori
   Pastikan terminal/Command Prompt Anda sudah berada di dalam direktori capstone-project-data-mining.

2. Instalasi Dependencies
   Sangat disarankan menggunakan virtual environment. Jalankan perintah berikut:
   pip install -r requirements.txt

3. Jalankan Aplikasi Web
   Jalankan perintah Streamlit berikut di terminal:
   streamlit run app/app.py
