import streamlit as st
import numpy as np

def show():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'IBM Plex Sans Thai', sans-serif; }

    .test-hero {
        background: linear-gradient(135deg, #0a1628 0%, #1a3a5c 50%, #0d2137 100%);
        border-radius: 16px; padding: 40px; margin-bottom: 28px;
        position: relative; overflow: hidden;
    }
    .test-hero::after {
        content: ''; position: absolute; bottom: -40px; right: -40px;
        width: 220px; height: 220px;
        background: radial-gradient(circle, rgba(56,189,248,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .test-badge {
        display: inline-block;
        background: rgba(56,189,248,0.2); border: 1px solid rgba(56,189,248,0.5);
        color: #bae6fd; padding: 4px 14px; border-radius: 20px;
        font-size: 0.75rem; font-weight: 600; letter-spacing: 0.08em;
        text-transform: uppercase; margin-bottom: 14px;
    }
    .test-hero h1 { color: #fff; font-size: 2rem; font-weight: 700; margin: 0 0 8px 0; }
    .test-hero p  { color: #7dd3fc; font-size: 0.95rem; margin: 0; font-weight: 300; }

    .input-card {
        background: #fff; border: 1px solid #e5e7eb;
        border-radius: 14px; padding: 22px 26px; margin-bottom: 14px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .input-card h4 {
        color: #0c2340; font-size: 1rem; font-weight: 700;
        margin: 0 0 14px 0; padding-bottom: 8px; border-bottom: 2px solid #e0f2fe;
    }

    .feat-summary {
        background: #f0f9ff; border: 1px solid #bae6fd;
        border-radius: 12px; padding: 18px 22px; margin-bottom: 18px;
    }
    .feat-summary h4 {
        color: #0369a1; font-size: 0.83rem; font-weight: 700;
        margin: 0 0 12px 0; text-transform: uppercase; letter-spacing: 0.06em;
    }
    .feat-row {
        display: flex; justify-content: space-between;
        padding: 5px 0; border-bottom: 1px dashed #bae6fd; font-size: 0.85rem;
    }
    .feat-row:last-child { border-bottom: none; }
    .feat-key { color: #6b7280; }
    .feat-val { color: #0c2340; font-weight: 600; font-family: 'IBM Plex Mono', monospace; }

    .result-survived {
        background: linear-gradient(135deg, #064e3b, #065f46);
        border: 1px solid #34d399; border-radius: 16px;
        padding: 28px; text-align: center; margin-top: 8px;
    }
    .result-died {
        background: linear-gradient(135deg, #450a0a, #7f1d1d);
        border: 1px solid #f87171; border-radius: 16px;
        padding: 28px; text-align: center; margin-top: 8px;
    }
    .result-icon  { font-size: 3rem; margin-bottom: 6px; }
    .result-label { font-size: 1.7rem; font-weight: 700; color: #fff; margin: 0 0 4px 0; }
    .result-sub   { color: rgba(255,255,255,0.65); font-size: 0.88rem; margin: 0 0 14px 0; }
    .prob-label   { color: rgba(255,255,255,0.55); font-size: 0.78rem; margin: 10px 0 3px 0; }
    .prob-val     { color: #fff; font-size: 1.35rem; font-weight: 700;
                    font-family: 'IBM Plex Mono', monospace; }
    .prob-bar-bg  { background: rgba(255,255,255,0.15); border-radius: 99px;
                    height: 10px; margin: 8px 0; overflow: hidden; }
    .prob-bar-s   { height: 100%; border-radius: 99px;
                    background: linear-gradient(90deg, #34d399, #10b981); }
    .prob-bar-d   { height: 100%; border-radius: 99px;
                    background: linear-gradient(90deg, #fca5a5, #ef4444); }

    .model-votes {
        background: rgba(255,255,255,0.08); border-radius: 10px;
        padding: 12px 16px; margin-top: 14px;
    }
    .model-votes p { color: rgba(255,255,255,0.6); font-size: 0.78rem;
                     margin: 0 0 8px 0; text-transform: uppercase; letter-spacing: 0.05em; }
    .vote-row { display: flex; justify-content: space-between; align-items: center;
                margin-bottom: 5px; }
    .vote-name { color: rgba(255,255,255,0.7); font-size: 0.82rem; }
    .vote-prob { color: #fff; font-size: 0.82rem; font-weight: 600;
                 font-family: 'IBM Plex Mono', monospace; }
    </style>
    """, unsafe_allow_html=True)

    # ── Hero ──────────────────────────────────────────────────────
    st.markdown("""
    <div class="test-hero">
        <div class="test-badge">ทดสอบโมเดล — ML Ensemble</div>
        <h1>🚢 ทดสอบการทำนาย Ensemble</h1>
        <p>กรอกข้อมูลผู้โดยสาร Titanic เพื่อให้โมเดล Ensemble (SVM + ANN + Random Forest)
        ทำนายว่าจะ <strong style="color:#a5f3fc;">รอดชีวิต</strong>
        หรือ <strong style="color:#fca5a5;">ไม่รอดชีวิต</strong></p>
    </div>
    """, unsafe_allow_html=True)

    # ── Load model ────────────────────────────────────────────────
    @st.cache_resource
    def load_artifacts():
        from train_models import train_ensemble
        model, scaler, features = train_ensemble()
        return model, scaler

    with st.spinner("⏳ กำลังเตรียมโมเดล (ครั้งแรกอาจใช้เวลาสักครู่)..."):
        try:
            model, scaler = load_artifacts()
        except Exception as e:
            st.error(f"❌ เกิดข้อผิดพลาด: {e}")
            return

    # ── Layout ───────────────────────────────────────────────────
    col_form, col_result = st.columns([1.1, 0.9], gap="large")

    with col_form:
        # Personal info
        st.markdown('<div class="input-card"><h4>👤 ข้อมูลส่วนตัว</h4>', unsafe_allow_html=True)
        pclass = st.selectbox("ชั้นโดยสาร (Pclass)",
            options=[1, 2, 3],
            format_func=lambda x: {1:"🥇 First Class", 2:"🥈 Second Class", 3:"🥉 Third Class"}[x])
        sex = st.radio("เพศ (Sex)", ["male", "female"],
            format_func=lambda x: "👨 Male — ชาย" if x == "male" else "👩 Female — หญิง",
            horizontal=True)
        age = st.slider("อายุ (Age)", min_value=1, max_value=80, value=29)
        title_input = st.selectbox("คำนำหน้าชื่อ (Title)",
            options=["Mr", "Mrs", "Miss", "Master", "Rare"],
            help="Mr=ผู้ชายทั่วไป, Mrs=ผู้หญิงแต่งงาน, Miss=ผู้หญิงโสด, Master=เด็กชาย, Rare=ยศ/ตำแหน่งพิเศษ")
        st.markdown('</div>', unsafe_allow_html=True)

        # Family & Travel
        st.markdown('<div class="input-card"><h4>👨‍👩‍👧 ครอบครัวและการเดินทาง</h4>', unsafe_allow_html=True)
        sibsp = st.number_input("พี่น้อง / คู่สมรสที่เดินทางด้วย (SibSp)", 0, 8, 0)
        parch = st.number_input("พ่อแม่ / ลูกที่เดินทางด้วย (Parch)", 0, 6, 0)
        embarked_input = st.selectbox("ท่าเรือที่ขึ้น (Embarked)",
            options=["S", "C", "Q"],
            format_func=lambda x: {"S":"🏴󠁧󠁢󠁥󠁮󠁧󠁿 S — Southampton","C":"🇫🇷 C — Cherbourg","Q":"🇮🇪 Q — Queenstown"}[x])
        st.markdown('</div>', unsafe_allow_html=True)

        # Fare & Cabin
        st.markdown('<div class="input-card"><h4>💰 ราคาตั๋วและห้องโดยสาร</h4>', unsafe_allow_html=True)
        fare = st.number_input("ราคาตั๋ว (Fare, £)", min_value=0.0, max_value=600.0, value=32.0, step=0.5)
        has_cabin = st.radio("มีข้อมูลห้องโดยสาร (Cabin)?", ["ไม่มี", "มี"],
            horizontal=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Encode features ──────────────────────────────────────────
    sex_enc      = 1 if sex == "male" else 0
    embarked_enc = {"C": 0, "Q": 1, "S": 2}[embarked_input]
    title_enc    = {"Master": 0, "Miss": 1, "Mr": 2, "Mrs": 3, "Rare": 4}[title_input]
    family_size  = sibsp + parch + 1
    is_alone     = 1 if family_size == 1 else 0
    has_cabin_enc= 1 if has_cabin == "มี" else 0

    # AgeBand
    if age <= 12:   age_band = 0
    elif age <= 18: age_band = 1
    elif age <= 35: age_band = 2
    elif age <= 60: age_band = 3
    else:           age_band = 4

    # FareBand (approximate quantile bins from training data)
    if fare <= 7.91:    fare_band = 0
    elif fare <= 14.45: fare_band = 1
    elif fare <= 31.0:  fare_band = 2
    else:               fare_band = 3

    # Feature order must match FEATURES list from training:
    # Pclass, Sex, Age, Fare, Embarked, Title, FamilySize, IsAlone, HasCabin, AgeBand, FareBand
    features = np.array([[pclass, sex_enc, age, fare, embarked_enc,
                          title_enc, family_size, is_alone, has_cabin_enc,
                          age_band, fare_band]])

    with col_result:
        st.markdown(f"""
        <div class="feat-summary">
            <h4>📋 Features ที่ส่งเข้าโมเดล</h4>
            <div class="feat-row"><span class="feat-key">Pclass</span><span class="feat-val">{pclass}</span></div>
            <div class="feat-row"><span class="feat-key">Sex</span><span class="feat-val">{sex_enc} ({sex})</span></div>
            <div class="feat-row"><span class="feat-key">Age</span><span class="feat-val">{age} → AgeBand={age_band}</span></div>
            <div class="feat-row"><span class="feat-key">Fare</span><span class="feat-val">{fare:.1f} → FareBand={fare_band}</span></div>
            <div class="feat-row"><span class="feat-key">Embarked</span><span class="feat-val">{embarked_enc} ({embarked_input})</span></div>
            <div class="feat-row"><span class="feat-key">Title</span><span class="feat-val">{title_enc} ({title_input})</span></div>
            <div class="feat-row"><span class="feat-key">FamilySize</span><span class="feat-val">{family_size}</span></div>
            <div class="feat-row"><span class="feat-key">IsAlone</span><span class="feat-val">{is_alone}</span></div>
            <div class="feat-row"><span class="feat-key">HasCabin</span><span class="feat-val">{has_cabin_enc} ({has_cabin})</span></div>
        </div>
        """, unsafe_allow_html=True)

        predict = st.button("🔮 ทำนายผล", type="primary", use_container_width=True)

        if predict:
            X_scaled = scaler.transform(features)
            pred     = int(model.predict(X_scaled)[0])
            proba    = model.predict_proba(X_scaled)[0]  # [p_died, p_survived]
            p_surv   = proba[1] * 100
            p_died   = proba[0] * 100

            # Individual model probabilities
            svm_p = model.estimators_[0].predict_proba(X_scaled)[0][1] * 100
            ann_p = model.estimators_[1].predict_proba(X_scaled)[0][1] * 100
            rf_p  = model.estimators_[2].predict_proba(X_scaled)[0][1] * 100

            if pred == 1:
                st.markdown(f"""
                <div class="result-survived">
                    <div class="result-icon">🎉</div>
                    <p class="result-label">รอดชีวิต (Survived)</p>
                    <p class="result-sub">โมเดลทำนายว่าผู้โดยสารคนนี้จะ<strong>รอดชีวิต</strong></p>
                    <p class="prob-label">ความน่าจะเป็นรอดชีวิต</p>
                    <p class="prob-val">{p_surv:.1f}%</p>
                    <div class="prob-bar-bg"><div class="prob-bar-s" style="width:{p_surv}%;"></div></div>
                    <div class="model-votes">
                        <p>ความน่าจะเป็นจากแต่ละโมเดล</p>
                        <div class="vote-row"><span class="vote-name">🔵 SVM</span><span class="vote-prob">{svm_p:.1f}%</span></div>
                        <div class="vote-row"><span class="vote-name">🟣 ANN</span><span class="vote-prob">{ann_p:.1f}%</span></div>
                        <div class="vote-row"><span class="vote-name">🟢 Random Forest</span><span class="vote-prob">{rf_p:.1f}%</span></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-died">
                    <div class="result-icon">💀</div>
                    <p class="result-label">ไม่รอดชีวิต (Did Not Survive)</p>
                    <p class="result-sub">โมเดลทำนายว่าผู้โดยสารคนนี้จะ<strong>ไม่รอดชีวิต</strong></p>
                    <p class="prob-label">ความน่าจะเป็นรอดชีวิต</p>
                    <p class="prob-val">{p_surv:.1f}%</p>
                    <div class="prob-bar-bg"><div class="prob-bar-d" style="width:{p_died}%;"></div></div>
                    <div class="model-votes">
                        <p>ความน่าจะเป็นจากแต่ละโมเดล</p>
                        <div class="vote-row"><span class="vote-name">🔵 SVM</span><span class="vote-prob">{svm_p:.1f}%</span></div>
                        <div class="vote-row"><span class="vote-name">🟣 ANN</span><span class="vote-prob">{ann_p:.1f}%</span></div>
                        <div class="vote-row"><span class="vote-name">🟢 Random Forest</span><span class="vote-prob">{rf_p:.1f}%</span></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("กรอกข้อมูลด้านซ้ายแล้วกดปุ่ม **ทำนายผล**")


if __name__ == "__main__":
    st.set_page_config(page_title="ML Ensemble Test", page_icon="🚢", layout="wide")
    show()
