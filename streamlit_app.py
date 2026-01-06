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
# ======================
# SIDEBAR LOGO ATAS
# ======================
st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        padding:10px 0 15px 0;
    ">
        <h2>🥗 SIKAPAN</h2>
        <p style="font-size:22px;">
            🍳 🐟 🥩 🥬 🍎
        </p>
        <hr>
    </div>
    """,
    unsafe_allow_html=True
)
menu = st.sidebar.radio(
    "📂 Menu",
    ["🏠 Beranda", "🐟 Kesegaran Ikan", "🥩 Kesegaran Daging"],
    key="menu_utama"
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
# ======================
# HALAMAN KESEGARAN DAGING
# ======================
elif menu == "🥩 Kesegaran Daging":

    st.markdown("## 🥩 Evaluasi Kesegaran Daging")

    jenis_daging = st.selectbox(
        "Jenis Daging",
        ["Daging Merah (Sapi/Kambing)", "Daging Putih (Ayam)"],
        key="jenis_daging"
    )

    warna = st.selectbox(
        "Warna Daging",
        ["Merah cerah / Putih segar", "Pucat", "Kecoklatan/Abu-abu"],
        key="warna_daging"
    )

    bau = st.selectbox(
        "Bau",
        ["Segar", "Agak asam", "Busuk"],
        key="bau_daging"
    )

    tekstur = st.selectbox(
        "Tekstur",
        ["Kenyal", "Agak lembek", "Lembek"],
        key="tekstur_daging"
    )

    lendir = st.selectbox(
        "Permukaan Daging",
        ["Tidak berlendir", "Sedikit berlendir", "Berlendir"],
        key="lendir_daging"
    )

    hari = st.number_input(
        "Lama Penyimpanan (hari)",
        min_value=0,
        step=1,
        key="hari_daging"
    )

    if st.button("🔍 Evaluasi Kelayakan Daging", key="eval_daging"):

        indikator = 0
        if warna != "Merah cerah / Putih segar":
            indikator += 1
        if bau != "Segar":
            indikator += 1
        if tekstur != "Kenyal":
            indikator += 1
        if lendir != "Tidak berlendir":
            indikator += 1

        batas = 2 if jenis_daging == "Daging Putih (Ayam)" else 3

        if bau == "Busuk" or lendir == "Berlendir" or hari > batas:
            st.error("❌ Daging TIDAK LAYAK digunakan")

            st.markdown("### ⚠️ Peringatan Keamanan")
            st.write(
                "Daging berisiko mengandung bakteri patogen "
                "seperti Salmonella atau E. coli."
            )

        elif indikator >= 2:
            st.warning("⚠️ Kualitas daging menurun")

        else:
            st.success("✅ Daging MASIH LAYAK digunakan")

        # ===== PENYIMPANAN =====
        st.markdown("### 🧊 Panduan Penyimpanan")
        st.write(
            "- Simpan pada suhu 0–4 °C\n"
            "- Bekukan jika tidak segera digunakan\n"
            "- Gunakan wadah tertutup rapat"
        )

        # ===== PENGOLAHAN =====
        st.markdown("### 🍳 Rekomendasi Pengolahan")
        st.write(
            "- Masak hingga suhu internal matang\n"
            "- Hindari konsumsi setengah matang\n"
            "- Cocok diolah dengan perebusan, pengukusan, atau pemanggangan"
        )
