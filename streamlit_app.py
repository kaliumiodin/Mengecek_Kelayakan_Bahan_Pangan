import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(
    page_title="FishFresh Advisor",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk tampilan menarik
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .sub-header {
        color: #A23B72;
        font-size: 1.5rem;
        margin-top: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 10px;
        background-color: #D4EDDA;
        border-left: 5px solid #28A745;
        margin: 1rem 0;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 10px;
        background-color: #FFF3CD;
        border-left: 5px solid #FFC107;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 10px;
        background-color: #E7F3FF;
        border-left: 5px solid #17A2B8;
        margin: 1rem 0;
    }
    .stButton>button {
        background-color: #2E86AB;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 2rem;
    }
    .fish-card {
        padding: 1rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Data ikan dan parameter
FISH_DATABASE = {
    "Salmon": {
        "parameters": {
            "Kesegaran (1-10)": 8,
            "Warna Daging": ["Merah Segar", "Pink", "Pucat"],
            "Tekstur": ["Elastis", "Lembut", "Lembek"],
            "Bau": ["Segar Laut", "Aman", "Bau Amis", "Bau Busuk"],
            "Mata Ikan": ["Jernih", "Keruh", "Cekung"]
        },
        "processing_methods": {
            "Dikukus": "Mempertahankan 90% omega-3, cocok untuk diet rendah lemak",
            "Dipanggang": "Mempertahankan 85% omega-3 dengan rasa smoky",
            "Sashimi": "Hanya jika kesegaran 9-10, nutrisi 100% terjaga",
            "Dibakar": "Mempertahankan 80% nutrisi dengan citarasa kaya"
        },
        "min_score": 35
    },
    "Tuna": {
        "parameters": {
            "Kesegaran (1-10)": 8,
            "Warna Daging": ["Merah Tua", "Merah Cerah", "Coklat"],
            "Tekstur": ["Padat", "Agak Padat", "Lembek"],
            "Bau Amonia": ["Tidak Ada", "Sedikit", "Kuat"],
            "Insang": ["Merah Segar", "Merah Tua", "Coklat"]
        },
        "processing_methods": {
            "Sashimi/Tataki": "Jika kesegaran ≥9, nutrisi maksimal",
            "Dipanggang": "Mempertahankan 85% protein",
            "Dikukus dengan Jahe": "Baik untuk tuna kurang segar",
            "Kalengan": "Untuk penyimpanan jangka panjang"
        },
        "min_score": 32
    },
    "Kakap Merah": {
        "parameters": {
            "Kesegaran (1-10)": 7,
            "Sisik": ["Mengkilap", "Kusam", "Rontok"],
            "Mata": ["Jernih", "Keruh", "Cekung"],
            "Insang": ["Merah Muda", "Merah Tua", "Abu-abu"],
            "Daging": ["Padat", "Lembut", "Lembek"]
        },
        "processing_methods": {
            "Digoreng": "Kulit crispy, daging lembut",
            "Dikukus": "Mempertahankan 95% nutrisi",
            "Asam Manis": "Untuk kesegaran sedang",
            "Pepes": "Aroma rempah menambah cita rasa"
        },
        "min_score": 28
    },
    "Gurame": {
        "parameters": {
            "Kesegaran (1-10)": 6,
            "Ukuran (kg)": ["≥1", "0.5-1", "<0.5"],
            "Bau Lumpur": ["Tidak Ada", "Sedikit", "Kuat"],
            "Warna": ["Cerah", "Kusam", "Pucat"],
            "Tekstur Daging": ["Padat", "Agak Padat", "Lembek"]
        },
        "processing_methods": {
            "Bakar": "Rendah minyak, aroma khas",
            "Goreng": "Kulit renyah, daging lembut",
            "Pesmol": "Dengan bumbu kuning",
            "Asam Padeh": "Untuk daerah Sumatra"
        },
        "min_score": 25
    },
    "Teri": {
        "parameters": {
            "Kesegaran (1-10)": 5,
            "Warna": ["Keperakan", "Kusam", "Kuning"],
            "Bau": ["Segar", "Amis Ringan", "Amis Kuat"],
            "Kekeruhan Air": ["Jernih", "Agak Keruh", "Sangat Keruh"],
            "Kepadatan": ["Padat", "Agak Padat", "Renggang"]
        },
        "processing_methods": {
            "Diasinkan": "Untuk penyimpanan lama",
            "Digoreng Kriuk": "Snack tinggi kalsium",
            "Balado": "Dengan bumbu pedas",
            "Dijadikan Terasi": "Jika kurang segar"
        },
        "min_score": 20
    }
}

def main():
    # Header dengan gradient
    st.markdown('<h1 class="main-header">🐟 FishFresh Advisor</h1>', unsafe_allow_html=True)
    st.markdown("### *Aplikasi Cerdas untuk Kelayakan dan Pengolahan Ikan*")
    
    # Sidebar
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3079/3079165.png", width=100)
        st.markdown("### **Navigasi**")
        selected_fish = st.selectbox(
            "Pilih Jenis Ikan",
            list(FISH_DATABASE.keys()),
            help="Pilih jenis ikan yang ingin diperiksa"
        )
        
        st.markdown("---")
        st.markdown("### **Tentang Aplikasi**")
        st.info("""
        Aplikasi ini membantu Anda:
        1. Menilai kelayakan ikan untuk diolah
        2. Memberikan saran pengolahan terbaik
        3. Mempertahankan nutrisi ikan
        """)
        
        st.markdown("---")
        st.markdown("**Dikembangkan oleh:**")
        st.caption("Tim FishFresh Advisor © 2024")
    
    # Konten utama
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f'<div class="sub-header">Parameter Kualitas Ikan {selected_fish}</div>', unsafe_allow_html=True)
        
        fish_data = FISH_DATABASE[selected_fish]
        scores = {}
        
        # Input parameter berdasarkan jenis ikan
        for param, default in fish_data["parameters"].items():
            if "Kesegaran" in param:
                scores[param] = st.slider(
                    param, 
                    min_value=1, 
                    max_value=10, 
                    value=default if isinstance(default, int) else 5,
                    help="1 = Tidak segar, 10 = Sangat segar"
                )
            elif isinstance(default, list):
                scores[param] = st.select_slider(
                    param,
                    options=default,
                    value=default[0]
                )
        
        # Tombol analisis
        analyze = st.button("🔄 Analisis Kelayakan & Saran Pengolahan", use_container_width=True)
    
    with col2:
        st.markdown('<div class="sub-header">Tips Kesegaran Ikan</div>', unsafe_allow_html=True)
        tips = {
            "Mata": "Jernih dan menonjol",
            "Insang": "Merah cerah, tidak gelap",
            "Bau": "Segar seperti laut",
            "Tekstur": "Elastis, kembali saat ditekan",
            "Sisik": "Melekat kuat dan mengkilap"
        }
        
        for tip, desc in tips.items():
            with st.expander(f"✓ {tip}"):
                st.caption(desc)
    
    # Hasil analisis
    if analyze:
        st.markdown("---")
        st.markdown(f'<div class="sub-header">Hasil Analisis untuk Ikan {selected_fish}</div>', unsafe_allow_html=True)
        
        # Kalkulasi skor
        total_score = 0
        score_details = []
        
        for param, value in scores.items():
            if "Kesegaran" in param:
                param_score = value * 3  # Bobot lebih tinggi untuk kesegaran
            elif isinstance(value, str):
                # Beri skor berdasarkan pilihan
                options = fish_data["parameters"][param]
                if value == options[0]:
                    param_score = 10
                elif value == options[1]:
                    param_score = 7
                else:
                    param_score = 3
            else:
                param_score = value
            
            total_score += param_score
            score_details.append({"Parameter": param, "Nilai": value, "Skor": param_score})
        
        # Tampilkan skor
        col_score1, col_score2, col_score3 = st.columns(3)
        
        with col_score1:
            st.metric("Total Skor", f"{total_score}/50")
        
        with col_score2:
            st.metric("Batas Kelayakan", fish_data["min_score"])
        
        with col_score3:
            if total_score >= fish_data["min_score"]:
                st.success("✅ LAYAK DIOLAH")
            else:
                st.error("❌ TIDAK LAYAK DIOLAH")
        
        # Grafik skor
        df_scores = pd.DataFrame(score_details)
        fig = px.bar(df_scores, x='Parameter', y='Skor', 
                    title='Detail Skor Parameter',
                    color='Skor',
                    color_continuous_scale='RdYlGn')
        st.plotly_chart(fig, use_container_width=True)
        
        # Rekomendasi pengolahan
        st.markdown('<div class="sub-header">💡 Rekomendasi Pengolahan</div>', unsafe_allow_html=True)
        
        if total_score >= fish_data["min_score"]:
            st.balloons()
            st.markdown('<div class="success-box">Ikan ini LAYAK diolah dengan rekomendasi berikut:</div>', unsafe_allow_html=True)
            
            # Tampilkan metode pengolahan berdasarkan skor
            methods = fish_data["processing_methods"]
            cols = st.columns(len(methods))
            
            for idx, (method, desc) in enumerate(methods.items()):
                with cols[idx]:
                    st.markdown(f"""
                    <div class="fish-card">
                        <h4>🍽️ {method}</h4>
                        <small>{desc}</small>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Saran khusus berdasarkan skor
            st.markdown("#### 📝 Tips Khusus:")
            if total_score > 40:
                st.info("""
                **Ikan Sangat Segar!** 
                - Olah dengan metode minimal (kukus/panggang) untuk mempertahankan nutrisi maksimal
                - Hindari menggoreng dengan minyak banyak
                - Bisa dikonsumsi sebagai sashimi (jika jenis ikan memungkinkan)
                """)
            elif total_score > 30:
                st.info("""
                **Ikan Cukup Segar**
                - Olah dengan bumbu rempah untuk meningkatkan cita rasa
                - Masak hingga matang sempurna
                - Baik untuk metode bakar atau pepes
                """)
            else:
                st.info("""
                **Ikan Segar Minimal**
                - Olah dengan bumbu kuat (kari, asam pedas)
                - Masak lebih lama untuk memastikan kematangan
                - Hindari konsumsi mentah
                """)
        else:
            st.markdown('<div class="warning-box">Ikan ini TIDAK DISARANKAN untuk diolah dengan alasan:</div>', unsafe_allow_html=True)
            st.warning("""
            ❌ Skor kesegaran di bawah standar
            ❌ Berpotensi mengandung bakteri berbahaya
            ❌ Nutrisi telah berkurang signifikan
            """)
            
            st.markdown("#### 🚫 Alternatif Jika Tetap Ingin Mengolah:")
            st.caption("""
            1. **Bersihkan ekstra** dengan air mengalir dan cuka
            2. **Rendam dalam jeruk nipis** 30 menit
            3. **Masak dengan suhu tinggi** dan waktu lama
            4. **Gunakan bumbu dominan** untuk menetralkan bau
            5. **Hindari konsumsi oleh anak-anak dan lansia**
            """)
    
    # Footer
    st.markdown("---")
    col_f1, col_f2, col_f3 = st.columns(3)
    
    with col_f1:
        st.markdown("**📊 Statistik Nutrisi Terjaga:**")
        st.progress(0.85 if analyze and total_score >= fish_data["min_score"] else 0.3)
    
    with col_f2:
        st.markdown("**👨‍🍳 Tingkat Kesulitan:**")
        st.caption("Mudah - Menengah")
    
    with col_f3:
        st.markdown("**⏱️ Waktu Penyajian:**")
        st.caption("15-30 menit")

if __name__ == "__main__":
    main()
