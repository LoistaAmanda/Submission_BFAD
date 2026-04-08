import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.title("Bike Sharing Dashboard")
st.markdown("Analisis penggunaan sepeda berdasarkan cuaca, waktu, dan pola distribusi")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv('main_data.csv')

# =========================
# MAPPING
# =========================
weather_map = {
    1: "Cerah",
    2: "Berawan",
    3: "Hujan Ringan",
    4: "Hujan Lebat"
}
df['weather'] = df['weathersit'].map(weather_map)

weekday_map = {
    0: "Minggu",
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumat",
    6: "Sabtu"
}
df['weekday_name'] = df['weekday'].map(weekday_map)

# =========================
# FILTER
# =========================
st.sidebar.header("Filter")

selected_weather = st.sidebar.multiselect(
    "Pilih Cuaca",
    options=df['weather'].dropna().unique(),
    default=df['weather'].dropna().unique()
)

df_filtered = df[df['weather'].isin(selected_weather)]

# =========================
# LAYOUT (2 KOLOM)
# =========================
col1, col2 = st.columns(2)

# =========================
# VISUALISASI 1 (CUACA)
# =========================
with col1:
    st.subheader("Pengaruh Cuaca")

    weather_group = df_filtered.groupby('weather')['cnt'].mean().reset_index()

    fig1, ax1 = plt.subplots()

    sns.barplot(
        data=weather_group,
        x='weather',
        y='cnt',
        palette='Purples',
        ax=ax1
    )

    ax1.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
    ax1.set_xlabel("Kondisi Cuaca")
    ax1.set_ylabel("Rata-rata Penyewaan")

    st.pyplot(fig1)

# =========================
# VISUALISASI 2 (HARI)
# =========================
with col2:
    st.subheader("Penyewaan Berdasarkan Hari")

    weekday_group = df_filtered.groupby('weekday_name')['cnt'].mean().reset_index()

    order = ["Minggu","Senin","Selasa","Rabu","Kamis","Jumat","Sabtu"]

    weekday_group['weekday_name'] = pd.Categorical(
        weekday_group['weekday_name'],
        categories=order,
        ordered=True
    )

    weekday_group = weekday_group.sort_values('weekday_name')

    fig2, ax2 = plt.subplots()

    sns.barplot(
        data=weekday_group,
        x='weekday_name',
        y='cnt',
        palette='Purples',
        ax=ax2
    )

    ax2.set_title("Rata-rata Penyewaan per Hari")
    ax2.set_xlabel("Hari")
    ax2.set_ylabel("Rata-rata Penyewaan")

    st.pyplot(fig2)

# =========================
# VISUALISASI 3 (DISTRIBUSI)
# =========================
st.subheader("Distribusi Penyewaan Sepeda")

fig3, ax3 = plt.subplots()

sns.histplot(
    df_filtered['cnt'],
    bins=30,
    color='green',
    ax=ax3
)

ax3.set_title("Distribusi Jumlah Penyewaan")
ax3.set_xlabel("Jumlah Penyewaan")
ax3.set_ylabel("Frekuensi")

st.pyplot(fig3)

# =========================
# DATA TABLE
# =========================
st.subheader("Data Preview")
st.dataframe(df_filtered.head())

