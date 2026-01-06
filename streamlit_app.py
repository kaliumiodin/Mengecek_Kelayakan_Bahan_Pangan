import streamlit as st

# ======================
# HEADER
# ======================
st.set_page_config(
    page_title="Cek Kesegaran Ikan",
    page_icon="🐟",
    layout="centered"
)

st.title("🐟 Aplikasi Cek Kesegaran Ikan")
st.markdown(
    "Aplikasi ini digunakan untuk mengevaluasi **kelayakan dan kesegaran ikan** "
    "berdasarkan parameter **organoleptik** dan **lama penyimpanan**."
)

st.divider()

# ======================
# INPUT DATA
# ======================
st.subheader("🔍 Parameter Pemeriksaan")

warna = st.selectbox(
    "🎨 Kondisi Warna Ikan",
    ["Normal", "Pucat", "Gelap"]
)

bau = st.selectbox(
    "👃 Kondisi Bau",
    ["Segar", "Agak Asam", "Busuk"]
)

tekstur = st.selectbox(
    "✋ Kondisi Tekstur",
    ["Normal", "Lembek]()

