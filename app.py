import streamlit as st
import ml_ensemble_page
import ml_ensemble_test_page
import neural_network_page
import neural_network_test_page

st.set_page_config(page_title="Project IS", page_icon="🥹", layout="wide")
st.title("🔥Welcome to my IS Project")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'IBM Plex Sans Thai', sans-serif; }
            
    .ml-hero {
        background: linear-gradient(135deg, #0a1628 0%, #1a3a5c 50%, #0d2137 100%);
        border-radius: 16px; padding: 40px; margin-bottom: 28px;
        position: relative; overflow: hidden;
    }
    .ml-hero::after {
        content: ''; position: absolute; top: -50px; right: -50px;
        width: 250px; height: 250px;
        background: radial-gradient(circle, rgba(56,189,248,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .ml-badge {
        display: inline-block;
        background: rgba(56,189,248,0.2); border: 1px solid rgba(56,189,248,0.5);
        color: #bae6fd; padding: 4px 14px; border-radius: 20px;
        font-size: 0.75rem; font-weight: 600; letter-spacing: 0.08em;
        text-transform: uppercase; margin-bottom: 14px;
    }
    .ml-hero h1 { color: #fff; font-size: 2rem; font-weight: 700; margin: 0 0 8px 0; }
    .ml-hero p  { color: #7dd3fc; font-size: 0.95rem; margin: 0; font-weight: 300; }
    </style>
    """, unsafe_allow_html=True)

# ================= TOP TABS =================
Introduction, Model1, ml_test, Model2, ann_test= st.tabs([
    "Introduction",
    "Machine Learning",
    "Machine Learning Test",
    "Neural Network",
    "Neural Network Test"
])

with Introduction : 
    st.markdown("""
    <div class="ml-hero">
        <h1>Introduction</h1>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;เว็บไซต์นี้จัดทำขึ้นเพื่อเป็นส่วนหนึ่งของโครงงานในรายวิชา Intelligent System 
        โดยมีวัตถุประสงค์เพื่อศึกษากระบวนการพัฒนาโมเดล Machine Learning แบบ Ensemble และ </p><p>Neural Network 
        ตั้งแต่การเตรียมข้อมูล การสร้างและประเมินผลโมเดล ตลอดจนการพัฒนาเว็บแอปพลิเคชันเพื่อสาธิตการทำงานของโมเดลที่พัฒนาขึ้น</p>
    </div>
    """, unsafe_allow_html=True)

with Model1 :
    ml_ensemble_page.show()

with ml_test :
    ml_ensemble_test_page.show()

with Model2 :
    neural_network_page.show()

with ann_test : 
    neural_network_test_page.show()