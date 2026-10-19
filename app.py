import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Dashboard Ekonomi Indonesia",
    page_icon="🇮🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS KUSTOM UNTUK TAMPILAN ---
st.markdown("""
    <style>
    .main-header { font-size: 2.5rem; color: #B22222; font-weight: bold; }
    .sub-header { font-size: 1.2rem; color: #555; }
    .metric-card { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #B22222; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: FILTER & NAVIGASI ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg", width=100)
    st.title("Navigasi Data")
    st.info("Dashboard ini menyajikan data terkini mengenai tekanan harga pangan dan energi yang viral, bersanding dengan indikator makro resmi.")
    
    # Simulasi filter wilayah
    wilayah = st.selectbox(
        "Pilih Fokus Wilayah:",
        ["Nasional", "Makassar (Sulsel)", "Bali (Denpasar)"]
    )
    
    st.divider()
    st.caption("Sumber: Kompas.id, Kemenkeu, BI, ANTARA (Oktober 2026)")

# --- HEADER UTAMA ---
st.markdown('<p class="main-header">🇮🇩 Dinamika Ekonomi Indonesia</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Antara Stabilitas Makro dan Tekanan Biaya Hidup Viral</p>', unsafe_allow_html=True)

st.write("---")

# --- METRIK UTAMA (KPI) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Pertumbuhan Ekonomi (Semester I 2026)",
        value="5.45%",
        delta="Stabil",
        help="Sumber: Kemenkeu (APBN KiTa Okt 2026)"
    )

with col2:
    st.metric(
        label="Inflasi (September 2026)",
        value="3.28%",
        delta="Dalam Target",
        delta_color="normal",
        help="Sumber: BPS/Kemenkeu"
    )

with col3:
    st.metric(
        label="Defisit APBN (% PDB)",
        value="1.24%",
        delta="Terkendali",
        help="Hingga September 2026, lebih baik dari target awal"
    )

with col4:
    st.metric(
        label="Harga Cabai Rawit (Makassar)",
        value="Rp 90.000/kg",
        delta="+350%",
        delta_color="inverse",
        help="Naik dari Rp 20.000/kg. Sumber: Kompas (14/10/2026)"
    )

st.write("---")

# --- BAGIAN 1: FENOMENA VIRAL (TEKANAN HARGA) ---
st.header("🔥 Fenomena Viral: Uang Rp 100.000 Tak Lagi Cukup")
st.write("""
Berdasarkan laporan lapangan di Makassar, daya beli masyarakat tergerus drastis. 
Ibu rumah tangga mengeluhkan lonjakan harga bahan pokok yang tidak sebanding dengan pendapatan.
""")

# Data simulasi untuk grafik perbandingan harga
data_harga = pd.DataFrame({
    'Komoditas': ['Cabai Rawit', 'Tomat', 'Labu Siam', 'Daging Sapi'],
    'Harga Lama (Rp)': [20000, 7000, 1666, 120000],
    'Harga Sekarang (Rp)': [90000, 15000, 7000, 150000]
})

# Visualisasi dengan Plotly
fig_harga = go.Figure(data=[
    go.Bar(name='Harga Lama/Stabil', x=data_harga['Komoditas'], y=data_harga['Harga Lama (Rp)'], marker_color='#636EFA'),
    go.Bar(name='Harga Sekarang (Okt 2026)', x=data_harga['Komoditas'], y=data_harga['Harga Sekarang (Rp)'], marker_color='#EF553B')
])
fig_harga.update_layout(barmode='group', title="Perbandingan Harga Bahan Pokok (Makassar)", yaxis_title="Harga (Rp)")
st.plotly_chart(fig_harga, use_container_width=True)

with st.expander("Lihat Detail Narasi Viral"):
    st.write("""
    **Kutipan Warga (Kompas.id):**
    > *"Biasanya kalau bawa 100.000 sudah banyak yang saya beli... Sekarang harga lombok kecil (cabai rawit) sudah 90.000 per kilogram."* — Irmayanti (38), Makassar.
    
    **Fenomena Sosial:** 
    Muncul tren *Downgrade Lifestyle* di media sosial, di mana kelas menengah mengurangi pengeluaran untuk gaya hidup (kopi, olahraga) dan beralih ke barang murah.
    """)

st.write("---")

# --- BAGIAN 2: KONTRAST DENGAN MAKRO & ENERGI ---
col_kiri, col_kanan = st.columns(2)

with col_kiri:
    st.header("⛽ Krisis Energi (Bali)")
    st.error("Kelangkaan BBM di Bali (Oktober 2026)")
    st.write("""
    Harga bensin eceran sempat melonjak hingga **Rp 200.000 - Rp 300.000 per liter** 
    akibat kelangkaan pasokan di SPBU resmi. Hal ini viral di media sosial karena 
    seorang turis asing tertawa getir melihat harga tersebut.
    """)
    
    # Grafik sederhana harga BBM
    fig_bbm = px.bar(
        x=["Harga Normal (Pertalite)", "Harga Eceran Krisis"],
        y=[10000, 250000],
        labels={'x': 'Jenis Harga', 'y': 'Rupiah per Liter'},
        title="Lonjakan Harga BBM Eceran di Bali",
        color=["Harga Normal (Pertalite)", "Harga Eceran Krisis"],
        color_discrete_map={"Harga Normal (Pertalite)": "green", "Harga Eceran Krisis": "red"}
    )
    st.plotly_chart(fig_bbm, use_container_width=True)

with col_kanan:
    st.header("📊 Stabilitas Fundamental (Makro)")
    st.success("Pemerintah: Fundamental Tetap Kuat")
    st.write("""
    Meskipun terjadi gejolak harga di lapangan, Kementerian Keuangan mencatat 
    arus modal masuk (capital inflow) ke SBN dan SRBI mencapai **> Rp 200 Triliun** 
    hingga awal Oktober 2026.
    """)
    
    # Data PMI Manufaktur
    st.metric("PMI Manufaktur (Sept 2026)", "52.4", "Ekspansi")
    st.progress(52.4 / 100, text="Level Ekspansi (>50)")
    
    st.write("""
    **Catatan:** Bank Dunia memproyeksikan ekonomi Indonesia tumbuh **5,2%** pada 2026, 
    ditopang oleh permintaan domestik yang kuat.
    """)

st.write("---")

# --- BAGIAN 3: ANALISIS KELAS MENENGAH ---
st.header("📉 Tekanan pada Kelas Menengah")

data_kelas = pd.DataFrame({
    'Kategori': ['Kelas Menengah (2018)', 'Kelas Menengah (2025)', 'Rentan Miskin (2018)', 'Rentan Miskin (2025)'],
    'Juta Jiwa': [60.8, 46.7, 68.5, 74.5]
})

fig_kelas = px.bar(
    data_kelas, 
    x='Kategori', 
    y='Juta Jiwa', 
    color='Kategori',
    title="Pergeseran Struktur Kelas Sosial (2018 vs 2025)",
    text_auto=True
)
st.plotly_chart(fig_kelas, use_container_width=True)

st.info("""
**Mengapa ini penting?** 
Penurunan jumlah kelas menengah dan naiknya kelompok rentan miskin menunjukkan bahwa inflasi dan PHK (63.789 pekerja Jan-Sep 2026) mulai menggerus daya beli kelas menengah yang menjadi tulang punggung konsumsi domestik.
""")

# --- FOOTER ---
st.write("---")
st.caption("Dibuat dengan Streamlit | Data dihimpun dari pemberitaan publik dan rilis resmi pemerintah (Oktober 2026).")