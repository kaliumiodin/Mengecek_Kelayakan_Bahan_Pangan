import streamlit as st

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="SIKAPAN - Kelayakan Bahan Pangan",
    page_icon="🥗",
    layout="wide"
)
# ======================
# SIDEBAR (LOGO + MENU)
# ======================
st.sidebar.markdown(
    """
    <div style="text-align:center;">
        <h2>🥗 SIKAPAN</h2>
        <p style="font-size:22px;">🍳 🐟 🥩 🥚 🥬 🍎</p>
        <hr>
    </div>
    """,
    unsafe_allow_html=True
)
menu = st.sidebar.radio(
    "📂 Menu",
    [
        "🏠 Beranda",
        "🐟 Kesegaran Ikan",
        "🥩 Kesegaran Daging",
        "🥚 Kesegaran Telur"
    ],
    key="menu_sidebar"
)
# ======================
# HEADER UTAMA
# ======================
st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #2e7d32, #66bb6a);
        padding:22px;
        border-radius:12px;
        text-align:center;
        color:white;
    ">
        <h1>🥗 SIKAPAN</h1>
        <p>Sistem Informasi Kelayakan dan Pengolahan Bahan Pangan</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")
# ======================
# BERANDA
# ======================
if menu == "🏠 Beranda":
    st.markdown(
        """
        <div style="background:#f1f8e9; padding:20px; border-radius:10px;">
            <p>
            Aplikasi <b>SIKAPAN</b> digunakan untuk mengevaluasi kelayakan bahan pangan
            berdasarkan indikator fisik sederhana serta memberikan rekomendasi keamanan pangan.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
# =====================
# HALAMAN IKAN
# ======================
elif menu == "🐟 Kesegaran Ikan":
    st.subheader("🐟 Evaluasi Kesegaran Ikan")

    jenis = st.selectbox("Jenis Ikan", ["Ikan Laut", "Ikan Tawar"])
    bau = st.selectbox("Bau", ["Segar", "Agak amis", "Busuk"])
    tekstur = st.selectbox("Tekstur Daging", ["Kenyal", "Agak lembek", "Lembek"])
    hari = st.number_input("Lama Penyimpanan (hari)", min_value=0, step=1)

    if st.button("🔍 Evaluasi Ikan"):
        batas = 2 if jenis == "Ikan Laut" else 3
        if bau == "Busuk" or tekstur == "Lembek" or hari > batas:
            st.error("❌ Ikan TIDAK LAYAK dikonsumsi")
        else:
            st.success("✅ Ikan MASIH LAYAK dikonsumsi")
# ======================
# HALAMAN DAGING
# ======================
elif menu == "🥩 Kesegaran Daging":
    st.subheader("🥩 Evaluasi Kesegaran Daging")

    jenis = st.selectbox("Jenis Daging", ["Ayam", "Sapi/Kambing"])
    bau = st.selectbox("Bau", ["Segar", "Agak asam", "Busuk"])
    lendir = st.selectbox("Permukaan", ["Tidak berlendir", "Berlendir"])
    hari = st.number_input("Lama Penyimpanan (hari)", min_value=0, step=1)

    if st.button("🔍 Evaluasi Daging"):
        batas = 2 if jenis == "Ayam" else 3
        if bau == "Busuk" or lendir == "Berlendir" or hari > batas:
            st.error("❌ Daging TIDAK LAYAK dikonsumsi")
        else:
            st.success("✅ Daging MASIH LAYAK dikonsumsi")
# ======================
# HALAMAN TELUR (HALAMAN BARU)
# ======================
elif menu == "🥚 Kesegaran Telur":
    st.subheader("🥚 Evaluasi Kesegaran Telur")

    bau = st.selectbox("Bau Telur", ["Tidak berbau", "Amis", "Busuk"])
    cangkang = st.selectbox(
        "Kondisi Cangkang",
        ["Utuh & bersih", "Retak", "Kotor/lendir"]
    )
    uji_air = st.selectbox(
        "Uji Apung",
        ["Tenggelam & rebah", "Tenggelam berdiri", "Mengapung"]
    )
    hari = st.number_input("Lama Penyimpanan (hari)", min_value=0, step=1)

    if st.button("🔍 Evaluasi Telur"):
        if bau == "Busuk" or uji_air == "Mengapung" or hari > 21:
            st.error("❌ Telur TIDAK LAYAK dikonsumsi")
        else:
            st.success("✅ Telur MASIH LAYAK dikonsumsi")
