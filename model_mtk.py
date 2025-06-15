import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Model Matematika Industri", layout="wide")

# Sidebar
st.sidebar.title("Instruksi")
st.sidebar.markdown("""
- Pilih tab sesuai model
- Masukkan data sesuai kasus
- Lihat hasil perhitungan & grafik
""")

# Tab Navigasi
tab1, tab2, tab3 = st.tabs(["🔧 Optimasi Produksi", "📦 Model EOQ", "⏳ Model Antrian"])

with tab1:
    st.header("Optimasi Produksi – Usaha Percetakan Banner")
    st.markdown("Banner Indoor (Rp25rb) | Banner Outdoor (Rp40rb)")

    x = np.linspace(0, 100, 200)
    y1 = (90 - 2 * x) / 3  # dari 2x + 3y <= 90
    y2 = (100 - 1 * x) / 2  # dari x + 2y <= 100

    fig, ax = plt.subplots()
    ax.plot(x, y1, label="2x + 3y ≤ 90")
    ax.plot(x, y2, label="x + 2y ≤ 100")
    ax.set_xlim((0, 50))
    ax.set_ylim((0, 50))
    ax.set_xlabel("Banner Indoor (x)")
    ax.set_ylabel("Banner Outdoor (y)")
    ax.legend()
    st.pyplot(fig)

    st.success("Solusi bisa dihitung dengan metode grafik / solver LP untuk hasil optimal.")

with tab2:
    st.header("Model Persediaan – EOQ untuk Tinta Printer")
    D = st.number_input("Permintaan Tahunan (D)", value=6000)
    S = st.number_input("Biaya Pemesanan (S)", value=80000)
    H = st.number_input("Biaya Penyimpanan (H)", value=4000)

    if st.button("Hitung EOQ"):
        eoq = np.sqrt((2 * D * S) / H)
        st.success(f"Jumlah pemesanan optimal (EOQ): {int(eoq)} unit")

with tab3:
    st.header("Model Antrian M/M/1 – Servis Laptop")
    lam = st.number_input("Tingkat kedatangan rata-rata (λ)", value=8.0)
    mu = st.number_input("Tingkat pelayanan rata-rata (μ)", value=10.0)

    if lam >= mu:
        st.error("λ harus lebih kecil dari μ agar sistem stabil.
