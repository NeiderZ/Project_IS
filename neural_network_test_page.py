import streamlit as st
import numpy as np

def show():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'IBM Plex Sans Thai', sans-serif; }

    .test-hero {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        border-radius: 16px; padding: 40px; margin-bottom: 28px;
        position: relative; overflow: hidden;
    }
    .test-hero::after {
        content: ''; position: absolute; bottom: -40px; left: -40px;
        width: 220px; height: 220px;
        background: radial-gradient(circle, rgba(99,102,241,0.2) 0%, transparent 70%);
        border-radius: 50%;
    }
    .test-badge {
        display: inline-block;
        background: rgba(99,102,241,0.3); border: 1px solid rgba(99,102,241,0.6);
        color: #e0e7ff; padding: 4px 14px; border-radius: 20px;
        font-size: 0.75rem; font-weight: 600; letter-spacing: 0.08em;
        text-transform: uppercase; margin-bottom: 14px;
    }
    .test-hero h1 { color: #fff; font-size: 2rem; font-weight: 700; margin: 0 0 8px 0; }
    .test-hero p  { color: #c4b5fd; font-size: 0.95rem; margin: 0; font-weight: 300; }

    .input-card {
        background: #ffffff; border: 1px solid #e5e7eb;
        border-radius: 14px; padding: 24px 28px; margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .input-card h4 {
        color: #1e1b4b; font-size: 1rem; font-weight: 700;
        margin: 0 0 16px 0; padding-bottom: 8px; border-bottom: 2px solid #ede9fe;
    }

    .feature-summary {
        background: #f8f7ff; border: 1px solid #ddd6fe;
        border-radius: 12px; padding: 18px 22px; margin-bottom: 20px;
    }
    .feature-summary h4 {
        color: #4c1d95; font-size: 0.85rem; font-weight: 700;
        margin: 0 0 12px 0; text-transform: uppercase; letter-spacing: 0.06em;
    }
    .feat-row {
        display: flex; justify-content: space-between;
        padding: 5px 0; border-bottom: 1px dashed #ede9fe; font-size: 0.85rem;
    }
    .feat-row:last-child { border-bottom: none; }
    .feat-key { color: #6b7280; }
    .feat-val { color: #1e1b4b; font-weight: 600; font-family: 'IBM Plex Mono', monospace; }

    .result-pass {
        background: linear-gradient(135deg, #064e3b, #065f46);
        border: 1px solid #34d399; border-radius: 16px;
        padding: 32px; text-align: center; margin-top: 8px;
    }
    .result-fail {
        background: linear-gradient(135deg, #450a0a, #7f1d1d);
        border: 1px solid #f87171; border-radius: 16px;
        padding: 32px; text-align: center; margin-top: 8px;
    }
    .result-icon  { font-size: 3.5rem; margin-bottom: 8px; }
    .result-label { font-size: 1.8rem; font-weight: 700; color: #fff; margin: 0 0 6px 0; }
    .result-sub   { color: rgba(255,255,255,0.7); font-size: 0.9rem; margin: 0 0 16px 0; }
    .prob-label   { color: rgba(255,255,255,0.6); font-size: 0.8rem; margin: 12px 0 4px 0; }
    .prob-val     { color: #fff; font-size: 1.4rem; font-weight: 700;
                    font-family: 'IBM Plex Mono', monospace; }
    .prob-bar-bg  {
        background: rgba(255,255,255,0.15); border-radius: 99px;
        height: 10px; margin: 8px 0; overflow: hidden;
    }
    .prob-bar-pass { height: 100%; border-radius: 99px;
                     background: linear-gradient(90deg, #34d399, #10b981); }
    .prob-bar-fail { height: 100%; border-radius: 99px;
                     background: linear-gradient(90deg, #fca5a5, #ef4444); }
    </style>
    """, unsafe_allow_html=True)

    # ── Hero ──────────────────────────────────────────────────────
    st.markdown("""
    <div class="test-hero">
        <div class="test-badge">ทดสอบโมเดล — Neural Network</div>
        <h1>🧪 ทดสอบการทำนาย ANN</h1>
        <p>กรอกข้อมูลนักเรียนด้านล่าง โมเดลจะทำนายว่านักเรียนจะ
        <strong style="color:#a5f3fc;">ผ่าน</strong> หรือ
        <strong style="color:#fca5a5;">ไม่ผ่าน</strong></p>
    </div>
    """, unsafe_allow_html=True)

    # ── Train model (cached — รันครั้งเดียวตอน startup) ──────────
    @st.cache_resource
    def load_artifacts():
        from train_models import train_ann
        return train_ann()

    with st.spinner("⏳ กำลังเตรียมโมเดล (ครั้งแรกอาจใช้เวลาสักครู่)..."):
        try:
            model, scaler = load_artifacts()
        except Exception as e:
            st.error(f"❌ เกิดข้อผิดพลาด: {e}")
            return

    # ── Input form ────────────────────────────────────────────────
    col_form, col_result = st.columns([1.1, 0.9], gap="large")

    with col_form:
        st.markdown('<div class="input-card"><h4>👤 ข้อมูลพื้นฐาน</h4>', unsafe_allow_html=True)
        gender = st.selectbox(
            "เพศ (Gender)",
            ["male", "female"],
            format_func=lambda x: "👦 Male — ชาย" if x == "male" else "👧 Female — หญิง"
        )
        race = st.selectbox(
            "กลุ่มชาติพันธุ์ (Race/Ethnicity)",
            ["group A", "group B", "group C", "group D", "group E"],
            index=2
        )
        parent_edu = st.selectbox(
            "ระดับการศึกษาของผู้ปกครอง (Parental Level of Education)",
            ["some high school", "high school", "some college",
             "associate's degree", "bachelor's degree", "master's degree"],
            index=2
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="input-card"><h4>🏠 สภาพแวดล้อม</h4>', unsafe_allow_html=True)
        lunch = st.radio(
            "ประเภทอาหารกลางวัน (Lunch)",
            ["standard", "free/reduced"],
            format_func=lambda x: "🍱 Standard — มาตรฐาน" if x == "standard" else "🆓 Free/Reduced — ลดราคา/ฟรี",
            horizontal=True
        )
        test_prep = st.radio(
            "คอร์สเตรียมสอบ (Test Preparation Course)",
            ["none", "completed"],
            format_func=lambda x: "❌ None — ไม่ได้เข้าร่วม" if x == "none" else "✅ Completed — เรียนครบแล้ว",
            horizontal=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="input-card"><h4>📝 คะแนนสอบ (0 – 100)</h4>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            math_score    = st.number_input("🔢 Math",    0, 100, 65)
        with c2:
            reading_score = st.number_input("📖 Reading", 0, 100, 68)
        with c3:
            writing_score = st.number_input("✏️ Writing", 0, 100, 66)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Compute derived features ──────────────────────────────────
    gender_enc     = 0 if gender == "male" else 1
    race_enc       = {"group A":0,"group B":1,"group C":2,"group D":3,"group E":4}[race]
    parent_enc     = {"some high school":0,"high school":1,"some college":2,
                      "associate's degree":3,"bachelor's degree":4,"master's degree":5}[parent_edu]
    lunch_enc      = 1 if lunch == "standard" else 0
    prepared_enc   = 1 if test_prep == "completed" else 0
    language_score       = (reading_score + writing_score) / 2
    stem_strength        = math_score - language_score
    reading_writing_diff = abs(reading_score - writing_score)
    average_score        = (math_score + reading_score + writing_score) / 3

    # !! Feature order ต้องตรงกับตอน train !!
    # X columns: gender | race/ethnicity | parental level of education | language_score | stem_strength | reading_writing_diff | lunch_quality | prepared
    features = np.array([[gender_enc, race_enc, parent_enc,
                          language_score, stem_strength, reading_writing_diff,
                          lunch_enc, prepared_enc]])

    with col_result:
        st.markdown(f"""
        <div class="feature-summary">
            <h4>📋 Features ที่ส่งเข้าโมเดล</h4>
            <div class="feat-row">
                <span class="feat-key">gender</span>
                <span class="feat-val">{gender_enc}&nbsp;&nbsp;({gender})</span>
            </div>
            <div class="feat-row">
                <span class="feat-key">race/ethnicity</span>
                <span class="feat-val">{race_enc}&nbsp;&nbsp;({race})</span>
            </div>
            <div class="feat-row">
                <span class="feat-key">parental level of education</span>
                <span class="feat-val">{parent_enc}&nbsp;&nbsp;({parent_edu})</span>
            </div>
            <div class="feat-row">
                <span class="feat-key">lunch_quality</span>
                <span class="feat-val">{lunch_enc}&nbsp;&nbsp;({lunch})</span>
            </div>
            <div class="feat-row">
                <span class="feat-key">prepared</span>
                <span class="feat-val">{prepared_enc}&nbsp;&nbsp;({test_prep})</span>
            </div>
            <div class="feat-row">
                <span class="feat-key">language_score</span>
                <span class="feat-val">{language_score:.1f}</span>
            </div>
            <div class="feat-row">
                <span class="feat-key">stem_strength</span>
                <span class="feat-val">{stem_strength:+.1f}</span>
            </div>
            <div class="feat-row">
                <span class="feat-key">reading_writing_diff</span>
                <span class="feat-val">{reading_writing_diff:.1f}</span>
            </div>
            <div class="feat-row" style="border-top:2px solid #ddd6fe; margin-top:6px; padding-top:8px;">
                <span class="feat-key">⭐ average_score (อ้างอิง)</span>
                <span class="feat-val">{average_score:.1f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        predict = st.button("🔮 ทำนายผลการเรียน", type="primary", use_container_width=True)

        if predict:
            X_scaled = scaler.transform(features)
            prob     = float(model.predict(X_scaled, verbose=0)[0][0])
            pct      = prob * 100

            if prob >= 0.5:
                st.markdown(f"""
                <div class="result-pass">
                    <div class="result-icon">🎉</div>
                    <p class="result-label">ผ่าน (Pass)</p>
                    <p class="result-sub">โมเดลทำนายว่านักเรียนคนนี้ <strong>ผ่าน</strong> เกณฑ์</p>
                    <p class="prob-label">ความน่าจะเป็น (Probability of Pass)</p>
                    <p class="prob-val">{pct:.1f}%</p>
                    <div class="prob-bar-bg">
                        <div class="prob-bar-pass" style="width:{pct}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-fail">
                    <div class="result-icon">📉</div>
                    <p class="result-label">ไม่ผ่าน (Fail)</p>
                    <p class="result-sub">โมเดลทำนายว่านักเรียนคนนี้ <strong>ไม่ผ่าน</strong> เกณฑ์</p>
                    <p class="prob-label">ความน่าจะเป็น (Probability of Pass)</p>
                    <p class="prob-val">{pct:.1f}%</p>
                    <div class="prob-bar-bg">
                        <div class="prob-bar-fail" style="width:{pct}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("กรอกข้อมูลด้านซ้ายแล้วกดปุ่ม **ทำนายผลการเรียน**")


# ── Standalone run ────────────────────────────────────────────
if __name__ == "__main__":
    st.set_page_config(page_title="ANN Test", page_icon="🧪", layout="wide")
    show()
