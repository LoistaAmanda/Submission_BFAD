import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bike Sharing Dashboard ", layout="wide")

st.title("Bike Sharing Analysis Dashboard (2011-2012)")

# =========================
# LOAD DATA
# =========================
df_day = pd.read_csv('dashboard/main_day_data.csv')
df_hour = pd.read_csv('dashboard/main_hour_data.csv')

# convert date
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

# =========================
# MAPPING CUACA
# =========================
weather_map = {
    1: "Cerah",
    2: "Berawan",
    3: "Hujan Ringan",
}

df_day['weather'] = df_day['weathersit'].map(weather_map)
df_hour['weather'] = df_hour['weathersit'].map(weather_map)

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("Filter")

# filter cuaca (untuk visualisasi 1)
selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=df_day['weather'].dropna().unique(),
    default=df_day['weather'].dropna().unique()
)

# filter tanggal (untuk visualisasi 2)
selected_date = st.sidebar.date_input(
    "Pilih Tanggal",
    value=df_hour['dteday'].min(),
    min_value=df_hour['dteday'].min(),
    max_value=df_hour['dteday'].max()
)

# =========================
# FILTER DATA
# =========================
df_day_filtered = df_day[df_day['weather'].isin(selected_weather)]
df_hour_filtered = df_hour[df_hour['dteday'] == pd.to_datetime(selected_date)]

st.subheader("Preview Data")

if st.checkbox("Tampilkan Data"):
    st.dataframe(df_hour_filtered.head(20))

# =========================
# LAYOUT
# =========================
col1, col2 = st.columns(2)

# =========================
# VISUALISASI 1 (CUACA)
# =========================
weather_map = {
    1:"Cerah", 
    2:"Berawan", 
    3:"Hujan Ringan"
}

df_day['weather'] = df_day['weathersit'].map(weather_map)

df_day_filtered = df_day[df_day['weather'].isin(selected_weather)]

weather_group = df_day_filtered.groupby('weather')['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(
    data=weather_group,
    x='weather',
    y='cnt',
    palette=['#E6E6FA','#CDB4DB','#9370DB','#4B0082'],
    edgecolor='black',
    ax=ax
)

ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca (2011–2012)")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan")
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()

st.pyplot(fig)

# =========================
# VISUALISASI 2 (JAM)
# =========================
df_hour_filtered = df_hour[
    df_hour['dteday'] == pd.to_datetime(selected_date)
]

hour_group = df_hour_filtered.groupby('hr')['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,5))

sns.lineplot(
    data=hour_group,
    x='hr',
    y='cnt',
    color='#006400',
    linewidth=2.5,
    ax=ax
)

ax.fill_between(
    hour_group['hr'],
    hour_group['cnt'],
    color='#90EE90',
    alpha=0.3
)

ax.set_title("Pola Penyewaan Sepeda Berdasarkan Jam (2011–2012)")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xticks(range(0,24))
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()

st.pyplot(fig)

# =========================
# INSIGHT DASHBOARD
# =========================
st.markdown("""
## insight
1. Cuaca yang cerah memiliki jumlah rata-rata penyewaan sepeda tertinggi 
2. Pada waktu sibuk seperti pagi dan sore hari, penggunaan sepeda mengalami peningkatan yang signifikan 
3. Sepeda cenderung digunakan sebagai mobilitas harian 
""")