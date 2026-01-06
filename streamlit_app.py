import streamlit as st

st.set_page_config(
    page_title="SIKAPAN - Kelayakan Bahan Pangan",
    page_icon="🥗",
    layout="wide"
)

# ===== HEADER WARNA =====
st.markdown(
    """
    <div style="background-color:#2e7d32; padding:20px; border-radius:10px">
        <h1 style="color:white; text-align:center;">🥗 SIKAPAN</h1>
        <h4 style="color:#e8f5e9; text-align:center;">
        Sistem Informasi Kelayakan dan Pengolahan Bahan Pangan
        </h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ===== KONTEN UTAMA =====
st.markdown(
    """
    <div style="background-color:#f1f8e9; padding:20px; border-radius:10px">
    <p style="font-size:16px;">
    Selamat datang di <b>SIKAPAN</b>, sebuah aplikasi berbasis web yang dirancang
    untuk membantu pengguna dalam menentukan kelayakan bahan pangan sebelum digunakan.
    Aplikasi ini menyediakan panduan mengenai kondisi bahan pangan, cara penyimpanan,
    serta rekomendasi pengolahan agar mutu dan kandungan gizi tetap terjaga.
    </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ===== TUJUAN =====
st.markdown(
    """
    <div style="background-color:#ffffff; padding:20px; border-left:6px solid #66bb6a">
    <h3>🎯 Tujuan Pengembangan Aplikasi</h3>
    <ul>
        <li>Memudahkan pengguna mengevaluasi kelayakan bahan pangan</li>
        <li>Memberikan panduan penyimpanan yang tepat</li>
        <li>Menyediakan rekomendasi pengolahan yang aman</li>
        <li>Mengurangi risiko penggunaan bahan pangan tidak layak</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ===== INFO =====
st.info(
    "👉 Gunakan menu navigasi untuk memilih jenis bahan pangan "
    "dan mendapatkan evaluasi serta rekomendasi yang sesuai."
)
