import streamlit as st
import pandas as pd
from PIL import Image

def run():
    # Main content
    st.title("Selamat datang!")
    img_url = "gambar.jpg"
    gambar = Image.open(img_url)
    st.image(gambar)
    # Dashboard Introduction
    st.markdown("""
    ### Dashboard apa ini?

    Dashboard interaktif ini menjelaskan tentang:
    - Memprediksi **harga pasar mobil** berdasarkan informasi mobil yang ada, seperti merk, model, tahun pembuatan, warna, hingga transmisi mobil.

    ---
    ### Latar Belakang Masalah
    Tujuan dari analisis ini adalah:
    - Mengetahui fitur-fitur atau variabel yang berpengaruh terhadap **prediksi harga pasar mobil**.
    - Mengolah data untuk membangun **model dengan akurasi tinggi dan error rendah** dalam prediksi harga.

    ---
    ### Model
    Algoritma yang digunakan dalam pemodelan **machine learning** kali ini adalah:
    - **XGBoost Regressor** untuk memprediksi **harga**.

    Model ini telah melalui proses **hyperparameter tuning** untuk meningkatkan performa. Nilai **R²** dari model ini adalah **91%**.
    """)

    # Dataset
    st.markdown("""
                
### Dataset
Dataset yang digunakan bersumber dari PT. AAAA.

**Kolom, tipe data, dan deskripsi dari dataset ini:**  

### Dataset Preview
Kolom, tipe, dan deskripsi data yang diolah:

Column Name         | Data Type | Description
-------------------|-----------|---------------------------------------------------------------
year               | INT64     | Tahun produksi kendaraan
make               | STRING    | Merek kendaraan (contoh: Toyota, Honda, BMW)
model              | STRING    | Model kendaraan (contoh: CR-V, Elantra, Malibu)
trim               | STRING    | Varian atau tipe trim kendaraan (contoh: EX, LTZ, Sport)
body               | STRING    | Jenis bodi kendaraan (contoh: Sedan, SUV, Hatchback)
transmission       | STRING    | Jenis transmisi kendaraan (Automatic / Manual)
vin                | STRING    | Nomor identifikasi kendaraan (Vehicle Identification Number)
branch             | STRING    | Lokasi cabang tempat kendaraan dijual (contoh: JAKARTA, SURABAYA)
condition          | FLOAT64   | Skor kondisi kendaraan (skala 0–50)
odometer           | FLOAT64   | Jarak tempuh kendaraan dalam kilometer
color              | STRING    | Warna eksterior kendaraan
interior           | STRING    | Warna interior kendaraan
seller             | STRING    | Nama atau tipe penjual kendaraan
marketprice        | FLOAT64   | Harga pasar kendaraan berdasarkan estimasi model
sellingprice       | FLOAT64   | Harga aktual kendaraan saat dijual
saledate           | STRING    | Tanggal penjualan kendaraan                                               |

---""")
    # Cara menggunakan dashboard
    st.markdown("""
    ---
    ### Cara Menggunakan Dashboard
    - Klik pilihan pada **sidebar** untuk membuat prediksi.
    - Cobalah untuk memasukkan berbagai macam data untuk mendapatkan hasil yang berbeda.

    Terima kasih sudah mengunjungi dashboard ini, sampai jumpa lagi di waktu yang akan datang!
    """)
