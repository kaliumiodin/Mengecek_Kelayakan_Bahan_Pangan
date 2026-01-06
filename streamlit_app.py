import streamlit as st

st.set_page_config(
    page_title="Kelayakan & Pengolahan Ikan",
    page_icon="🐟",
    layout="centered"
)

st.markdown(
    "<h1 style='text-align:center;'>🐟 Kelayakan & Rekomendasi Pengolahan Ikan</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:gray;'>Aplikasi berbasis parameter organoleptik & jenis ikan</p>",
    unsafe_allow_html=True
)

st.markdown("---")

with st.form("form_ikan"):
    jenis_ikan = st.selectbox(
        "🐠 Jenis Ikan",
        ["Ikan Berlemak", "Ikan Daging Putih", "Ikan Air Tawar", "Ikan Kecil"]
    )

    warna = st.selectbox("🎨 Warna", ["Normal", "Pucat", "Gelap"])
    bau = st.selectbox("👃 Bau", ["Segar", "Agak Asam", "Busuk"])
    tekstur = st.selectbox("✋ Tekstur", ["Normal", "Lembek", "Berlendir"])
    hari = st.number_input("📦 Lama Penyimpanan (hari)", 0, 14, 0)

    submit = st.form_submit_button("🔍 Evaluasi")

# ======================
# LOGIKA SISTEM
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
    st.subheader("📊 Hasil Analisis")

    if bau == "Busuk" or tekstur == "Berlendir" or hari > batas_simpan[jenis_ikan]:
        st.error("❌ IKAN TIDAK LAYAK DIOlah")
        st.write("🔎 Terjadi indikasi pembusukan.")
        st.write("❌ Tidak disarankan untuk dikonsumsi.")

    elif indikator >= 2:
        st.warning("⚠️ IKAN KURANG LAYAK")
        st.write("🍳 Disarankan diolah dengan **pemanasan sempurna**.")
        st.write("👉 Rekomendasi: Digoreng atau dimasak berkuah.")

    else:
        st.success("✅ IKAN LAYAK DIOlah")
        st.write("🥗 Kandungan gizi masih optimal.")
        st.write("👉 Rekomendasi terbaik:")
        st.write("- Kukus")
        st.write("- Pepes")
        st.write("- Tumis cepat")

    st.markdown("---")
    st.caption("Aplikasi ini bersifat edukatif dan tidak menggantikan uji laboratorium.")

