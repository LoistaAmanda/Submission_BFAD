# Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek

Proyek ini berfokus pada analisis pola penggunaan layanan bike sharing dengan berdasarkan pada faktor cuaca dan waktu pada rentang tahun 2011-2012. Dengan pemanfaatan dataset Bike sharing  serta hasilnya divisualisasikan dalam format dashboard yang interaktif menggunakan Streamlit.

Cakupan dalam proses analisis data secara menyeluruh dimulai dengan data wrangling sampai dengan pembuatan dashboard sebagai penyampaian insight.
---

## Dataset

Dataset yang digunakan terdiri dari dua bagian:

- day.csv: Data penyewaan sepeda per hari, digunakan untuk analisis berbasis cuaca  
- hour.csv: Data penyewaan sepeda per jam, digunakan untuk analisis berbasis waktu dan hari  

Sumber dataset:
https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset

---

## Pertanyaan Bisnis

- Pertanyaan 1: Bagaimana perbedaan jumlah penyewa sepeda di berbagai kondisi cuaca selama rentang tahun 2011-2012, dan kondisi cuaca yang paling optimal untuk meningkatkan jumlah penggunaan?

- Pertanyaan 2: Pada jam berapa terjadinya lonjakan penyewaan sepeda dalam satu hari dalam rentang tahun 2011-2012, dan bagaimana pola tersebut dapat mempengaruhi perilaku mobilitas pengguna?

---

## Setup Virtual Environment

Membuat virtual environment:

```bash
python -m venv venv
```

Mengaktifkan virtual environment:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

## Instalasi Library

Install semua library yang dibutuhkan menggunakan file requirements.txt:

```bash
pip install -r requirements.txt
```

Disarankan menggunakan requirements.txt agar dependency sesuai dengan kebutuhan proyek dan tidak perlu instalasi manual satu per satu.

---

## Menjalankan Dashboard

Masuk ke folder dashboard:

```bash
cd dashboard
```

Jalankan aplikasi:

```bash
streamlit run dashboard.py
```

---


## Proses Analisis

Tahapan analisis yang dilakukan dalam proyek ini meliputi:

1. Data Wrangling
   - Gathering Data
   - Assessing Data
   - Cleaning Data

2. Exploratory Data Analysis (EDA)

3. Data Visualization dan Explanatory Analysis

4. Analisis Lanjutan  
   Pengelompokan kategori dimulai dari Low, Medium, serta High menggunakan pendekatan quantile dilakukan dengan tujuan untuk mengelompokkan 3 kelompok yang proporsional, sehingga kategori-kategori tersebut dapat mempresentasikan tingkat penggunaan sepeda secara akurat dan sesuai dengan distribusi data yang ada

5. Conclusion
   - Hasil analisis data bike sharing selama periode 2011 sampai dengan 2012 menunjukkan penggunaan sepeda tidak hanya terjadi begitu saja terdapat pola yang terbentuk melalui keterkaitan antara kondisi lingkungan serta kebiasaan pengguna itu sendiri. 

   - Terdapat suatu penemuan yang menonjol dalam hasil analisis ini ialah pengaruh cuaca terhadap keputusan pengguna ketika cuaca cerah serta kondisi yang mendukung jumlah penyewa cenderung meningkat secara drastis. dan sebaliknya pada hujan atau cuaca buruk. hai ini menunjukkan bahwa kenyamanan serta rasa aman sangat menjadi pertimbangan yang tidak bisa diabaikan oleh pengguna sepeda. 

   - Selain berdasarkan cuaca ditemukan juga pola yang cukup konsisten pada waktu-waktu tertentu naiknya penggunaan sepeda, yaitu pada pagi dan sore hari. 

   - Faktor cuaca dan waktu saling mempengaruhi satu sama lain untuk menentukan tingkat penggunaan sepeda contohnya penggunaan tertinggi muncul ketika jam sibuk bertepatan dengan cuaca yang cerah sebaliknya jika diluar jam sibuk dan cuaca yang tidak bersahabat.

   - dari hasil analisis di atas ini menegaskan bahwa layanan Biken sharing mempunyai pola penggunaan yang bisa diprediksi. Hal ini sangat berguna dalam pengambilan keputusan operasi.
---

## Insight Utama

   - Cuaca yang cerah memiliki jumlah rata-rata penyewaan sepeda tertinggi 
   - Pada waktu sibuk seperti pagi dan sore hari, penggunaan sepeda mengalami peningkatan yang signifikan 
   - Sepeda cenderung digunakan sebagai mobilitas harian  

---

## Dashboard

Dashboard dibuat menggunakan Streamlit untuk menyajikan hasil analisis secara interaktif.

Fitur dashboard meliputi:

- Visualisasi pengaruh cuaca terhadap jumlah penyewaan sepeda  
- Visualisasi penyewaan berdasarkan jam  
- Distribusi pola penyewaan dalam satu hari  
- Filter berdasarkan kondisi cuaca  
- Filter berdasarkan tanggal  
- Tampilan data dalam bentuk tabel (preview data)  


URL: https://bike-sharing-dashboard-loistamnda1124.streamlit.app/
---
