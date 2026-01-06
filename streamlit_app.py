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

st.set_page_config(
    page_title="SIKAPAN - Kelayakan Bahan Pangan",
    page_icon="🥗",
    layout="wide"
)

# ================= SIDEBAR =================
st.sidebar.title("🔎 Navigasi")
menu = st.sidebar.radio(
    "Pilih halaman:",
    ["🏠 Beranda", "🐟 Kesegaran Ikan"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "SIKAPAN membantu mengevaluasi kelayakan "
    "bahan pangan dan memberikan rekomendasi pengolahan."
)

# ================= BERANDA =================
if menu == "🏠 Beranda":
    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg, #2e7d32, #66bb6a);
            padding:25px;
            border-radius:12px;
            text-align:center;
        ">
            <h1 style="color:white;">🥗 SIKAPAN</h1>
            <p style="color:rgba(255,255,255,0.9); font-size:18px;">
            Sistem Informasi Kelayakan dan Pengolahan Bahan Pangan
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div style="
            background-color: rgba(102,187,106,0.12);
            padding:22px;
            border-radius:12px;
            color: inherit;
        ">
        <p>
        Selamat datang di <b>SIKAPAN</b>. Aplikasi ini dirancang untuk membantu
        pengguna dalam menentukan kelayakan bahan pangan sebelum diolah atau dikonsumsi.
        </p>
        <p>
        Gunakan menu di sebelah kiri untuk memilih jenis bahan pangan
        dan memperoleh evaluasi kesegaran serta rekomendasi pengolahan.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= HALAMAN IKAN =================
elif menu == "🐟 Kesegaran Ikan":
    st.header("🐟 Evaluasi Kesegaran Ikan")

    st.markdown(
        """
        <div style="
            background-color: rgba(33,150,243,0.08);
            padding:20px;
            border-radius:12px;
            color: inherit;
        ">
        Halaman ini digunakan untuk mengevaluasi kesegaran ikan
        berdasarkan parameter organoleptik dan lama penyimpanan.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ===== INPUT PARAMETER =====
    col1, col2 = st.columns(2)

    with col1:
        warna = st.selectbox(
            "Kondisi Warna",
            ["Cerah / Mengkilap", "Agak Pucat", "Kusam / Gelap"]
        )

        bau = st.selectbox(
            "Kondisi Bau",
            ["Segar", "Agak Asam", "Busuk"]
        )

    with col2:
        tekstur = st.selectbox(
            "Kondisi Tekstur",
            ["Kenyal", "Agak Lembek", "Lembek / Berlendir"]()
