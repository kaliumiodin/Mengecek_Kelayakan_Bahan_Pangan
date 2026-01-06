import streamlit as st

st.set_page_config(
    page_title="SIKAPAN - Kelayakan Bahan Pangan",
    page_icon="🥗",
    layout="wide"
)

# ===== HEADER =====
st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #2e7d32, #66bb6a);
        padding:25px;
        border-radius:12px;
        text-align:center;
    ">
        <h1 style="margin-bottom:5px; color:white;">
            🥗 SIKAPAN
        </h1>
        <p style="font-size:18px; color:rgba(255,255,255,0.9);">
            Sistem Informasi Kelayakan dan Pengolahan Bahan Pangan
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ===== KONTEN UTAMA =====
st.markdown(
    """
    <div style="
        background-color: rgba(102, 187, 106, 0.12);
        padding:22px;
        border-radius:12px;
        color: inherit;
        font-size:16px;
    ">
        <p>
        Selamat datang di <b>SIKAPAN</b>, sebuah aplikasi berbasis web yang dirancang
        untuk membantu pengguna dalam menentukan kelayakan bahan pangan sebelum digunakan.
        </p>
        <p>
        Aplikasi ini memberikan panduan kondisi bahan pangan, teknik penyimpanan yang tepat,
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
    <div style="
        background-color: rgba(0,0,0,0.02);
        padding:22px;
        border-left:6px solid #66bb6a;
        border-radius:10px;
        color: inherit;
    ">
        <h3>🎯 Tujuan Aplikasi</h3>
        <ul>
            <li>Memudahkan evaluasi kelayakan bahan pangan</li>
            <li>Memberikan panduan penyimpanan yang benar</li>
            <li>Menyarankan metode pengolahan yang aman</li>
            <li>Mengurangi risiko konsumsi bahan pangan tidak layak</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ===== INFO =====
st.info(
    "👉 Gunakan menu navigasi di sidebar untuk memilih jenis bahan pangan "
    "dan mendapatkan evaluasi serta rekomendasi yang sesuai."
)
