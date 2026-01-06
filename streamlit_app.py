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

menu = st.sidebar.radio(
    "📂 Menu",
    ["🏠 Beranda", "🐟 Kesegaran Ikan"]
)

st.set_page_config(
    page_title="SIKAPAN - Kelayakan Bahan Pangan",
    page_icon="🐟",
    layout="wide"
)

# ===== SIDEBAR =====
menu = st.sidebar.radio(
    "📂 Menu",
    ["🏠 Beranda", "🐟 Kesegaran Ikan"]
)

# =========================
# ===== HALAMAN IKAN =====
# =========================
if menu == "🐟 Kesegaran Ikan":

    st.markdown("## 🐟 Evaluasi Kesegaran Ikan")

    jenis_ikan = st.selectbox(
        "Jenis Ikan",
        ["Ikan Laut", "Ikan Tawar"]
    )

    warna_insang = st.selectbox(
        "Warna Insang",
        ["Merah cerah", "Merah pucat", "Coklat keabu-abuan"]
    )

    bau = st.selectbox(
        "Bau",
        ["Segar", "Agak amis", "Busuk"]
    )

    tekstur = st.selectbox(
        "Tekstur Daging",
        ["Kenyal", "Agak lembek", "Lembek"]
    )

    mata = st.selectbox(
        "Kondisi Mata",
        ["Jernih & menonjol", "Agak keruh", "Keruh & cekung"]
    )

    hari = st.number_input(
        "Lama Penyimpanan (hari)",
        min_value=0,
        step=1
    )

    if st.button("🔍 Evaluasi Kelayakan"):

        indikator_buruk = 0

        if warna_insang != "Merah cerah":
            indikator_buruk += 1
        if bau != "Segar":
            indikator_buruk += 1
        if tekstur != "Kenyal":
            indikator_buruk += 1
        if mata != "Jernih & menonjol":
            indikator_buruk += 1

        batas_hari = 2 if jenis_ikan == "Ikan Laut" else 3

        if bau == "Busuk" or tekstur == "Lembek" or hari > batas_hari:
            st.error("❌ Ikan TIDAK LAYAK digunakan")

            st.markdown("### ⚠️ Peringatan Keamanan")
            st.write(
                "Ikan berpotensi mengandung mikroorganisme berbahaya "
                "dan tidak aman untuk dikonsumsi."
            )

        elif indikator_buruk >= 2:
            st.warning("⚠️ Kualitas ikan menurun")

        else:
            st.success("✅ Ikan MASIH LAYAK digunakan")

        # ===== REKOMENDASI =====
        st.markdown("### 🧊 Panduan Penyimpanan")
        st.write(
            "- Simpan pada suhu 0–4 °C\n"
            "- Gunakan wadah tertutup\n"
            "- Hindari kontak langsung dengan air"
        )

        st.markdown("### 🍳 Rekomendasi Pengolahan")
        st.write(
            "- Olah dengan pemanasan sempurna\n"
            "- Cocok untuk dikukus, direbus, atau digoreng\n"
            "- Hindari konsumsi mentah jika kualitas menurun"
        )
