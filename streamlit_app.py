import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="FishFresh Advisor",
    page_icon="🐟",
    layout="wide"
)

# Data ikan (versi sederhana)
FISH_DATABASE = {
    "Salmon": {
        "parameters": ["Kesegaran", "Warna", "Tekstur", "Bau", "Mata"],
        "min_score": 35
    },
    "Tuna": {
        "parameters": ["Kesegaran", "Warna", "Tekstur", "Bau", "Insang"],
        "min_score": 32
    },
    "Kakap Merah": {
        "parameters": ["Kesegaran", "Sisik", "Mata", "Insang", "Daging"],
        "min_score": 28
    }
}

def main():
    st.title("🐟 FishFresh Advisor")
    st.markdown("### Aplikasi Analisis Kelayakan Ikan")
    
    # Pilih ikan
    selected_fish = st.selectbox("Pilih Jenis Ikan:", list(FISH_DATABASE.keys()))
    
    st.markdown("---")
    st.subheader(f"Parameter untuk Ikan {selected_fish}")
    
    # Input nilai
    scores = {}
    fish_data = FISH_DATABASE[selected_fish]
    
    for param in fish_data["parameters"]:
        if param == "Kesegaran":
            scores[param] = st.slider(f"{param} (1-10)", 1, 10, 5)
        else:
            scores[param] = st.select_slider(
                f"{param}",
                options=["Buruk", "Cukup", "Baik", "Sangat Baik"],
                value="Baik"
            )
    
    # Tombol analisis
    if st.button("Analisis Kelayakan", type="primary"):
        # Hitung total skor
        total_score = 0
        for param, value in scores.items():
            if param == "Kesegaran":
                total_score += value * 3
            elif value == "Sangat Baik":
                total_score += 10
            elif value == "Baik":
                total_score += 7
            elif value == "Cukup":
                total_score += 4
            else:
                total_score += 1
        
        st.markdown("---")
        st.subheader("Hasil Analisis")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Skor", total_score)
            st.metric("Batas Minimum", fish_data["min_score"])
        
        with col2:
            if total_score >= fish_data["min_score"]:
                st.success("✅ LAYAK DIOLAH")
                st.balloons()
            else:
                st.error("❌ TIDAK LAYAK")
        
        # Rekomendasi
        st.markdown("### 💡 Rekomendasi Pengolahan")
        
        if total_score >= fish_data["min_score"]:
            if total_score > 40:
                st.info("""
                **Rekomendasi:** Dikukus atau Dipanggang
                **Alasan:** Mempertahankan 90% nutrisi, cocok untuk ikan segar
                """)
            elif total_score > 30:
                st.info("""
                **Rekomendasi:** Dibakar atau Pepes
                **Alasan:** Bumbu rempah meningkatkan cita rasa
                """)
            else:
                st.info("""
                **Rekomendasi:** Digoreng dengan bumbu kuat
                **Alasan:** Menetralkan bau dan memastikan kematangan
                """)
        else:
            st.warning("""
            **Tidak disarankan untuk diolah.** 
            Jika tetap ingin mengolah:
            1. Bersihkan dengan air mengalir
            2. Rendam dalam jeruk nipis 30 menit
            3. Masak dengan suhu tinggi
            """)

if __name__ == "__main__":
    main()
