import streamlit as st

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="Kelayakan Ikan",
    page_icon="🐟",
    layout="centered"
)

st.title("🐟 Aplikasi Kelayakan & Pengolahan Ikan")
st.caption("Berbasis parameter organoleptik dan jenis ikan")

st.markdown("---")

# ======================
# FORM INPUT
# ======================
with st.form("form_kelayakan"):
    jenis_ikan = st.selectbox(
        "🐠 Jenis Ikan",
        (
            "Ikan Berlemak",
            "Ikan Daging Putih",
            "Ikan Air Tawar",
            "Ikan Kecil"
        )
    )

    warna = st.selectbox(
        "🎨 Warna Ikan",
        ("Normal", "Pucat", "Gelap")
    )

    bau = st.selectbox(
        "👃 Bau Ikan",
        ("Segar", "Agak Asam", "Busuk")
    )

    tekstur = st.selectbox(
        "✋ Tekstur Ikan",
        ("Normal", "Lembek", "Berlendir")
    )

    hari = st.number_input(
        "📦 Lama Penyimpanan (hari)",
        min_value=0,
        max_value=14,
        step=1
    )

    submit = st.form_submit_button("🔍 Evaluasi Kelayakan")

# ======================
# LOGIKA PENILAIAN
# ======================
if submit:
    indikator = 0

    if warna != "Normal":
        indikator += 1
    if bau != "Segar":
        indikator += 1
    if tekstur != "Normal":
        indikator += 1

    batas_simpan = {
        "Ikan Berlemak": 3,
        "Ikan Daging Putih": 5,
        "Ikan Air Tawar": 4,
        "Ikan Kecil": 2
    }

    st.markdown("---")
    st.subheader("📊 Hasil Evaluasi")

    if bau == "Busuk" or tekstur == "Berlendir" or hari > batas_simpan[jenis_ikan]:
        st.error("❌ IKAN TIDAK LAYAK DIOlah")
        st.write("Terjadi indikasi pembusukan.")
        st.write("❌ Tidak disarankan untuk dikonsumsi.")

    elif indikator >= 2:
        st.warning("⚠️ IKAN KURANG LAYAK")
        st.write("Disarankan diolah dengan pemanasan sempurna.")
        st.write("🍳 Rekomendasi: digoreng atau dimasak berkuah.")

    else:
        st.success("✅ IKAN LAYAK DIOlah")
        st.write("Kandungan gizi masih relatif baik.")
        st.write("🥗 Rekomendasi pengolahan:")
        st.write("- Kukus")
        st.write("- Pepes")
        st.write("- Tumis cepat")

    st.markdown("---")
    st.caption("Aplikasi bersifat edukatif dan tidak menggantikan uji laboratorium.")
