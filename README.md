# Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek

Proyek ini berfokus pada analisis pola penggunaan layanan bike sharing dengan berdasarkan pada faktor cuaca dan waktu. Dengan pemanfaatan dataset Bike sharing  serta hasilnya divisualisasikan dalam format dashboard yang interaktif menggunakan Streamlit.

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

- Pertanyaan 1: Bagaimana kondisi cuaca dapat mempengaruhi jumlah penyewaan sepeda?
- Pertanyaan 2: Kapan jumlah penyewaan sepeda tertinggi berdasarkan waktu (jam)?

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
   Dilakukan pengelompokan data menggunakan metode binning untuk mengelompokkan jumlah penyewaan ke dalam kategori Low, Medium, dan High.

5. Conclusion
- Conclution pertanyaan 1: Pengaruh kondisi cuaca memiliki pengaruh yang signifikan terhadap jumlah penyewaan sepeda. penyewaan sepeda tertinggi terjadi saat kondisi cuaca cerah, sedangkan pada kondisi cuaca buruk, jumlah penyewaan sepeda cenderung menurun. Hal ini menunjukan bahwa penguna penyewa sepeda lebih suka menggunakan sepeda ketika kondisi mendukung.

- Conclution pertanyaan 2: Waktu penyewaan sepeda tertinggi per harinya. penyewaan sepeda mencapai titik tertinggi pada jam sibuk yaitu saat pagi (pukul 7-9) dan sore (pukul 16-18). pola ini menunjukan bahwa sepeda banyak digunakan sebagai alat transportasi untuk beraktivitas berangkat dan pulang kerja.
---

## Insight Utama

- Penyewaan sepeda tertinggi terjadi pada kondisi cuaca cerah  
- Terdapat dua puncak penggunaan sepeda, yaitu pada pagi hari dan sore hari  
- Faktor cuaca dan waktu merupakan dua faktor utama yang memengaruhi penggunaan layanan bike sharing  

---

## Dashboard

Dashboard dibuat menggunakan Streamlit untuk menyajikan hasil analisis secara interaktif.

Fitur dashboard meliputi:

- Visualisasi pengaruh cuaca terhadap jumlah penyewaan sepeda  
- Visualisasi penyewaan berdasarkan hari  
- Distribusi jumlah penyewaan  
- Filter berdasarkan kondisi cuaca  
- Tampilan data dalam bentuk tabel  


URL: https://bike-sharing-dashboard-loistamnda.streamlit.app/
---
