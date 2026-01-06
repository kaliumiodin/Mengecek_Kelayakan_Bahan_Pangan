import streamlit as st

st.title("Aplikasi Cek Kelayakan Bahan Pangan")

warna = st.selectbox(
    "Pilih kondisi warna",
    ["Normal", "Pucat", "Gelap"]

bau = st.selectbox(
    "Pilih kondisi bau",
    ["Segar", "Agak Asam", "Busuk"]

tekstur = st.selectbox(
    "Pilih kondisi tekstur",
    ["Normal", "Lembek", "Berlendir"]

hari = st.number_input(
    "Lama penyimpanan (hari)",
    min_value=0,
    step=1

if st.button("Cek Kelayakan"):
    indikator_buruk = 0

    if warna != "Normal":
        indikator_buruk += 1
    if bau != "Segar":
        indikator_buruk += 1
    if tekstur != "Normal":
        indikator_buruk += 1

    if bau == "Busuk" or tekstur == "Berlendir" or hari > 7:
        st.error("❌ Bahan pangan TIDAK LAYAK konsumsi")
        st.write("Rekomendasi: Jangan dikonsumsi")
    elif indikator_buruk >= 2:
        st.warning("⚠️ Bahan pangan TIDAK LAYAK konsumsi")
        st.write("Rekomendasi: Sebaiknya dibuang")
    else:
        st.success("✅ Bahan pangan MASIH LAYAK konsumsi")
        st.write("Rekomendasi: Simpan dengan baik dan konsumsi segera")
