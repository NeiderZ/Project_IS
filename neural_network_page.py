import streamlit as st

def show():
    # ─── Custom CSS ───────────────────────────────────────────────
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans Thai', sans-serif;
    }

    /* ── Hero Banner ── */
    .nn-hero {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        border-radius: 16px;
        padding: 48px 40px;
        margin-bottom: 32px;
        position: relative;
        overflow: hidden;
    }
    .nn-hero::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 280px; height: 280px;
        background: radial-gradient(circle, rgba(139,92,246,0.25) 0%, transparent 70%);
        border-radius: 50%;
    }
    .nn-hero h1 {
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0 0 8px 0;
        line-height: 1.2;
    }
    .nn-hero p {
        color: #c4b5fd;
        font-size: 1.05rem;
        margin: 0;
        font-weight: 300;
    }
    .nn-badge {
        display: inline-block;
        background: rgba(139,92,246,0.3);
        border: 1px solid rgba(139,92,246,0.6);
        color: #ddd6fe;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 16px;
    }

    /* ── Section Cards ── */
    .section-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 28px 32px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .section-card h3 {
        color: #1e1b4b;
        font-size: 1.2rem;
        font-weight: 700;
        margin: 0 0 16px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid #ede9fe;
    }
    .section-card p, .section-card li {
        color: #374151;
        font-size: 0.95rem;
        line-height: 1.8;
    }

    /* ── Step Badge ── */
    .step-row {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        margin-bottom: 18px;
    }
    .step-num {
        background: linear-gradient(135deg, #7c3aed, #4f46e5);
        color: white;
        width: 32px; height: 32px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.85rem;
        font-weight: 700;
        flex-shrink: 0;
        margin-top: 2px;
    }
    .step-content strong {
        color: #1e1b4b;
        font-weight: 600;
        display: block;
        margin-bottom: 4px;
    }
    .step-content span {
        color: #6b7280;
        font-size: 0.88rem;
    }

    /* ── Feature Tags ── */
    .tag-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
    .tag {
        background: #f3f4f6;
        border: 1px solid #d1d5db;
        color: #374151;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.82rem;
        font-family: 'IBM Plex Mono', monospace;
    }
    .tag.purple {
        background: #ede9fe; border-color: #c4b5fd; color: #5b21b6;
    }
    .tag.green {
        background: #d1fae5; border-color: #6ee7b7; color: #065f46;
    }
    .tag.red {
        background: #fee2e2; border-color: #fca5a5; color: #991b1b;
    }

    /* ── Architecture Diagram ── */
    .arch-diagram {
        background: #0f0c29;
        border-radius: 12px;
        padding: 28px;
        font-family: 'IBM Plex Mono', monospace;
    }
    .arch-layer {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 6px;
    }
    .layer-box {
        background: rgba(139,92,246,0.25);
        border: 1px solid rgba(139,92,246,0.6);
        color: #ddd6fe;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        min-width: 180px;
        text-align: center;
    }
    .layer-box.input  { border-color: #34d399; background: rgba(52,211,153,0.1); color: #34d399; }
    .layer-box.output { border-color: #f87171; background: rgba(248,113,113,0.1); color: #f87171; }
    .layer-arrow { color: #6b7280; font-size: 1.1rem; }
    .layer-note  { color: #9ca3af; font-size: 0.78rem; }

    /* ── Metric Cards ── */
    .metric-row { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 16px; }
    .metric-card {
        flex: 1; min-width: 120px;
        background: linear-gradient(135deg, #1e1b4b, #312e81);
        border-radius: 10px;
        padding: 18px 20px;
        text-align: center;
    }
    .metric-card .val {
        color: #c4b5fd;
        font-size: 1.6rem;
        font-weight: 700;
        font-family: 'IBM Plex Mono', monospace;
    }
    .metric-card .lbl {
        color: #a5b4fc;
        font-size: 0.8rem;
        margin-top: 4px;
    }

    /* ── Reference List ── */
    .ref-item {
        display: flex; gap: 10px;
        padding: 10px 0;
        border-bottom: 1px solid #f3f4f6;
        color: #374151;
        font-size: 0.88rem;
        line-height: 1.6;
    }
    .ref-num {
        color: #7c3aed;
        font-weight: 700;
        font-family: 'IBM Plex Mono', monospace;
        min-width: 28px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ─── Hero ─────────────────────────────────────────────────────
    st.markdown("""
    <div class="nn-hero">
        <div class="nn-badge">Model 2 — Neural Network</div>
        <h1>Artificial Neural Network (ANN)</h1>
        <p>การพัฒนาโมเดล Deep Learning สำหรับทำนายผลการเรียนของนักเรียน<br>
        ด้วย Binary Classification บน Students Performance in Exams Dataset</p>
    </div>
    """, unsafe_allow_html=True)

    # ─── Tabs ─────────────────────────────────────────────────────
    t1, t2, t3, t4, t5 = st.tabs([
        "📦 Dataset",
        "🔧 เตรียมข้อมูล",
        "📐 ทฤษฎี ANN",
        "🏗️ พัฒนาโมเดล",
        "📚 อ้างอิง"
    ])

    # ════════════════════════════════════════════════════════════════
    # TAB 1 — Dataset
    # ════════════════════════════════════════════════════════════════
    with t1:
        st.markdown("""
        <div class="section-card">
            <h3>📦 ที่มาของ Dataset</h3>
            <p>
                Dataset ที่ใช้ในโมเดลนี้คือ <strong>Students Performance in Exams</strong>
                ซึ่งดาวน์โหลดมาจากเว็บไซต์
                <a href="https://www.kaggle.com/datasets/spscientist/students-performance-in-exams" target="_blank">Kaggle</a>
                (spscientist/students-performance-in-exams) โดย Dataset นี้รวบรวมข้อมูล
                ของนักเรียน 1,000 คน เพื่อศึกษาว่าปัจจัยต่าง ๆ ส่งผลต่อคะแนนสอบอย่างไร
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="section-card">
                <h3>🗂️ Features ของ Dataset</h3>
                <div class="step-row">
                    <div class="step-num">1</div>
                    <div class="step-content">
                        <strong>gender</strong>
                        <span>เพศของนักเรียน (male / female)</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num">2</div>
                    <div class="step-content">
                        <strong>race/ethnicity</strong>
                        <span>กลุ่มชาติพันธุ์ (group A–E)</span>
                        <br>
                        <span>*เนื่องจากผู้สร้าง dataset ตั้งใจปกปิดข้อมูลเชื้อชาติจริงของนักเรียน เพื่อเหตุผลด้านความเป็นส่วนตัวและจริยธรรม จึงใช้เป็น (group A - E)</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num">3</div>
                    <div class="step-content">
                        <strong>parental level of education</strong>
                        <span>ระดับการศึกษาของผู้ปกครอง (some high school → master's degree)</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num">4</div>
                    <div class="step-content">
                        <strong>lunch</strong>
                        <span>ประเภทอาหารกลางวัน (standard / free/reduced)</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num">5</div>
                    <div class="step-content">
                        <strong>test preparation course</strong>
                        <span>เข้าร่วมคอร์สเตรียมสอบหรือไม่ (none / completed)</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num">6</div>
                    <div class="step-content">
                        <strong>math / reading / writing score</strong>
                        <span>คะแนนสอบแต่ละวิชา (0–100)</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="section-card">
                <h3>⚠️ ความไม่สมบูรณ์ของข้อมูล</h3>
                <p>Dataset มีความไม่สมบูรณ์ดังนี้ ซึ่งต้องผ่านกระบวนการเตรียมข้อมูลก่อนนำไปฝึกโมเดล</p>
                <div class="tag-row">
                    <span class="tag red">Missing Values บางเซลล์</span>
                    <span class="tag red">ข้อมูลซ้ำกัน (Duplicate Rows)</span>
                    <span class="tag red">Categorical ยังไม่ได้ Encode</span>
                    <span class="tag red">ช่วงค่าของ Features ต่างกัน (ยังไม่ Normalize)</span>
                    <span class="tag red">ไม่มี Target Column โดยตรง</span>
                </div>
                <br>
                <p><strong>Target Variable ที่สร้างขึ้น:</strong></p>
                <div class="tag-row">
                    <span class="tag purple">final_pass = 1 (Pass)</span>
                    <span class="tag purple">final_pass = 0 (Fail)</span>
                </div>
                <p style="margin-top:10px; color:#6b7280; font-size:0.85rem;">
                    กำหนดว่าหาก average_score ≥ 50 ถือว่าผ่าน (Pass)
                </p>
            </div>
            """, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    # TAB 2 — Data Preparation
    # ════════════════════════════════════════════════════════════════
    with t2:
        st.markdown("""
        <div class="section-card">
            <h3>🔧 กระบวนการเตรียมข้อมูล (Data Preparation)</h3>
        </div>
        """, unsafe_allow_html=True)

        steps = [
            ("1", "ตรวจสอบ Missing Values",
             "ใช้ <code>df.isnull().any()</code> เพื่อหาคอลัมน์ที่มีข้อมูลว่าง "
             "จากนั้นตรวจสอบจำนวนแถวที่หายไปเพื่อตัดสินใจว่าจะลบหรือ Impute"),
            ("2", "ลบข้อมูลซ้ำ (Drop Duplicates)",
             "ใช้ <code>df.drop_duplicates()</code> เพื่อลบแถวที่มีข้อมูลซ้ำกันทุกคอลัมน์ "
             "พร้อม <code>reset_index()</code> เพื่อ reset ลำดับ index"),
            ("3", "Feature Engineering",
             "สร้าง Feature ใหม่เพื่อช่วยให้โมเดลเรียนรู้ได้ดีขึ้น เช่น "
             "<code>average_score</code>, <code>language_score</code>, "
             "<code>stem_strength</code>, <code>reading_writing_diff</code> "
             "และ pass flag ของแต่ละวิชา"),
            ("4", "Encoding Categorical Variables",
             "แปลงข้อมูลประเภท Categorical เป็นตัวเลขด้วย Label Mapping เช่น "
             "gender → {male:0, female:1}, lunch → {standard:1, free/reduced:0}, "
             "parental education → 0–5, race/ethnicity → 0–4"),
            ("5", "สร้าง Target Variable",
             "สร้างคอลัมน์ <code>final_pass</code> จาก <code>average_score ≥ 50</code> "
             "เพื่อใช้เป็น Label สำหรับ Binary Classification"),
            ("6", "แบ่ง Train/Test Split",
             "แบ่งข้อมูล 80:20 ด้วย <code>train_test_split</code> "
             "(test_size=0.2, random_state=42) พร้อมระวัง Data Leakage "
             "โดย Drop คอลัมน์คะแนนดิบออกก่อน"),
            ("7", "Feature Scaling (StandardScaler)",
             "ปรับขนาด Feature ด้วย <code>StandardScaler</code> "
             "เพื่อให้ค่าเฉลี่ย = 0 และ Std = 1 "
             "สำคัญสำหรับ Neural Network เพราะ Gradient Descent จะ Converge เร็วขึ้น"),
        ]

        for num, title, desc in steps:
            st.markdown(f"""
            <div class="section-card" style="margin-bottom:12px; padding:18px 24px;">
                <div class="step-row" style="margin-bottom:0;">
                    <div class="step-num">{num}</div>
                    <div class="step-content">
                        <strong style="font-size:1rem;">{title}</strong>
                        <span style="font-size:0.9rem; line-height:1.7;">{desc}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <h3>🛡️ การป้องกัน Data Leakage</h3>
            <p>
                ก่อน train โมเดล จำเป็นต้อง Drop คอลัมน์ที่อาจทำให้เกิด Data Leakage ได้แก่
                <code>math score</code>, <code>reading score</code>, <code>writing score</code>,
                <code>average_score</code>, <code>pass_math</code>, <code>pass_reading</code>,
                <code>pass_writing</code>, <code>pass_all</code>
                เนื่องจากคอลัมน์เหล่านี้เป็น <strong>ข้อมูลที่มาจาก Target โดยตรง</strong>
                ทำให้โมเดลเรียนรู้ได้โดยไม่มีความหมายจริง
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    # TAB 3 — Theory
    # ════════════════════════════════════════════════════════════════
    with t3:
        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown("""
            <div class="section-card">
                <h3>Artificial Neural Network</h3>
                <p>
                    <strong>Artificial Neural Network (ANN)</strong> หรือโครงข่ายประสาทเทียม
                    เป็นโมเดล Machine Learning
                    ประกอบด้วย <strong>Neuron</strong> (โหนด) จำนวนมากที่เชื่อมต่อกันเป็นชั้น ๆ
                </p>
                <p>
                    เหมาะกับปัญหาที่ข้อมูลที่มีความซับซ้อน ที่ไม่เป็นเชิงเส้นได้ดี
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="section-card">
                <h3>📐 โครงสร้างของ ANN</h3>
                <div class="step-row">
                    <div class="step-num" style="background: linear-gradient(135deg,#059669,#10b981);">I</div>
                    <div class="step-content">
                        <strong>Input Layer</strong>
                        <span>รับค่า Feature ทุกตัวเป็น Input โดยจำนวน Neuron = จำนวน Feature</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num">H</div>
                    <div class="step-content">
                        <strong>Hidden Layers</strong>
                        <span>ชั้นซ่อน ทำหน้าที่แปลง Feature ให้เป็น Representation ที่ซับซ้อนขึ้น
                        แต่ละ Neuron รับ Input จาก Layer ก่อนหน้าผ่าน Weight และ Bias</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num" style="background: linear-gradient(135deg,#dc2626,#ef4444);">O</div>
                    <div class="step-content">
                        <strong>Output Layer</strong>
                        <span>สำหรับ Binary Classification มี 1 Neuron ใช้ Sigmoid Activation
                        เพื่อให้ผลลัพธ์อยู่ในช่วง [0, 1]</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="section-card">
                <h3>⚡ Activation Functions</h3>
                <div class="step-row">
                    <div class="step-num">R</div>
                    <div class="step-content">
                        <strong>ReLU (Rectified Linear Unit)</strong>
                        <span>f(x) = max(0, x) — ใช้ใน Hidden Layers เพราะช่วยแก้ปัญหา Vanishing Gradient
                        และ Computationally Efficient</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num">S</div>
                    <div class="step-content">
                        <strong>Sigmoid</strong>
                        <span>f(x) = 1 / (1 + e⁻ˣ) — ใช้ใน Output Layer
                        แปลงค่าให้อยู่ระหว่าง 0–1 เหมาะกับ Binary Classification</span>
                    </div>
                </div>
                <div class="step-row">
                    <div class="step-num">A</div>
                    <div class="step-content">
                        <strong>Adam Optimizer</strong>
                        <span>Adaptive Moment Estimation ปรับ Learning Rate อัตโนมัติต่อแต่ละ Parameter
                        มีประสิทธิภาพสูงกว่า SGD ทั่วไป</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="section-card">
                <h3>📉 Loss Function & Training</h3>
                <p>
                    ใช้ <strong>Binary Cross-Entropy</strong> เป็น Loss Function
                    เนื่องจากเป็นปัญหา Binary Classification:
                </p>
                <p style="text-align:center; font-family:'IBM Plex Mono',monospace;
                           background:#f3f4f6; padding:10px; border-radius:6px;
                           font-size:0.85rem; color:#1e1b4b;">
                    L = −[y·log(ŷ) + (1−y)·log(1−ŷ)]
                </p>
                <p>
                    กระบวนการ <strong>Backpropagation</strong> จะคำนวณ Gradient ของ Loss
                    เทียบกับ Weight ในแต่ละ Layer แล้วปรับค่า Weight ผ่าน Adam Optimizer
                    ทำซ้ำกัน 50 Epochs
                </p>
            </div>
            """, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    # TAB 4 — Model Development
    # ════════════════════════════════════════════════════════════════
    with t4:
        st.markdown("""
        <div class="section-card">
            <h3>🏗️ สถาปัตยกรรมของโมเดล ANN</h3>
            <p>โมเดลถูกออกแบบให้มี 4 ชั้น (3 Hidden + 1 Output) เหมาะสมกับขนาดข้อมูลประมาณ 1,000 แถว
            และ Feature จำนวน 8 ตัว</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="arch-diagram">
            <div class="arch-layer">
                <div class="layer-box input">Input Layer (8 nodes)</div>
                <div class="layer-note">← 8 Features: gender, race, parent_edu, lunch_quality,<br>&nbsp;&nbsp;&nbsp;prepared, language_score, stem_strength, reading_writing_diff</div>
            </div>
            <div style="margin-left:70px; color:#6b7280; font-size:1.2rem; margin: 6px 0 6px 70px;">↓</div>
            <div class="arch-layer">
                <div class="layer-box">Hidden Layer 1 (32 nodes)</div>
                <div class="layer-note">← Activation: ReLU · เรียนรู้ Pattern ระดับ Low-level</div>
            </div>
            <div style="margin-left:70px; color:#6b7280; font-size:1.2rem; margin: 6px 0 6px 70px;">↓</div>
            <div class="arch-layer">
                <div class="layer-box">Hidden Layer 2 (16 nodes)</div>
                <div class="layer-note">← Activation: ReLU · Compress Representation</div>
            </div>
            <div style="margin-left:70px; color:#6b7280; font-size:1.2rem; margin: 6px 0 6px 70px;">↓</div>
            <div class="arch-layer">
                <div class="layer-box">Hidden Layer 3 (8 nodes)</div>
                <div class="layer-note">← Activation: ReLU · Abstract Features ระดับสูง</div>
            </div>
            <div style="margin-left:70px; color:#6b7280; font-size:1.2rem; margin: 6px 0 6px 70px;">↓</div>
            <div class="arch-layer">
                <div class="layer-box output">Output Layer (1 node)</div>
                <div class="layer-note">← Activation: Sigmoid → ค่า 0–1 (ผ่าน threshold 0.5 → Pass/Fail)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="section-card">
                <h3>⚙️ Hyperparameters</h3>
                <div class="tag-row">
                    <span class="tag purple">Optimizer: Adam</span>
                    <span class="tag purple">Loss: Binary Cross-Entropy</span>
                    <span class="tag purple">Epochs: 50</span>
                    <span class="tag purple">Batch Size: 32</span>
                    <span class="tag purple">Validation Split: 20%</span>
                    <span class="tag green">Framework: TensorFlow / Keras</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="section-card">
                <h3>📊 ผลการประเมินโมเดล</h3>
                <div class="metric-row">
                    <div class="metric-card">
                        <div class="val">~95%</div>
                        <div class="lbl">Test Accuracy</div>
                    </div>
                    <div class="metric-card">
                        <div class="val">50</div>
                        <div class="lbl">Epochs</div>
                    </div>
                    <div class="metric-card">
                        <div class="val">8</div>
                        <div class="lbl">Input Features</div>
                    </div>
                </div>
                <p style="color:#6b7280; font-size:0.82rem; margin-top:12px;">
                    * ค่า Accuracy อาจเปลี่ยนแปลงได้ตาม Dataset และ Random State
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <h3>💻 Source Code สำหรับสร้างโมเดล</h3>
        </div>
        """, unsafe_allow_html=True)

        st.code("""
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ── แบ่ง Features และ Target ──────────────────────────────────
X = df.drop(columns=["final_pass", "average_score", "pass_all",
                      "math score", "reading score", "writing score",
                      "pass_math", "pass_reading", "pass_writing"])
y = df["final_pass"]

# ── Train/Test Split 80:20 ────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Feature Scaling ───────────────────────────────────────────
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ── สร้าง ANN Model ───────────────────────────────────────────
model = Sequential([
    Dense(32, activation="relu", input_shape=(X_train.shape[1],)),
    Dense(16, activation="relu"),
    Dense(8,  activation="relu"),
    Dense(1,  activation="sigmoid")
])

# ── Compile ───────────────────────────────────────────────────
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# ── Train ─────────────────────────────────────────────────────
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2
)

# ── Evaluate ──────────────────────────────────────────────────
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")
        """, language="python")

    # ════════════════════════════════════════════════════════════════
    # TAB 5 — References
    # ════════════════════════════════════════════════════════════════
    with t5:
        st.markdown("""
        <div class="section-card">
            <h3>📚 แหล่งอ้างอิง</h3>
        </div>
        """, unsafe_allow_html=True)

        refs = [
            ("[1]", "spscientist. (2018). <em>Students Performance in Exams</em>. Kaggle Dataset.",
             "https://www.kaggle.com/datasets/spscientist/students-performance-in-exams"),
            ("[2]", "Goodfellow, I., Bengio, Y., & Courville, A. (2016). <em>Deep Learning</em>. MIT Press.",
             "https://www.deeplearningbook.org/"),
            ("[3]", "Chollet, F. (2021). <em>Deep Learning with Python</em> (2nd ed.). Manning Publications.",
             "https://www.manning.com/books/deep-learning-with-python-second-edition"),
            ("[4]", "TensorFlow Documentation. <em>tf.keras.layers.Dense</em>. Google.",
             "https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense"),
            ("[5]", "Kingma, D. P., & Ba, J. (2015). <em>Adam: A Method for Stochastic Optimization</em>. ICLR.",
             "https://arxiv.org/abs/1412.6980"),
            ("[6]", "Scikit-learn Developers. <em>StandardScaler Documentation</em>.",
             "https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html"),
            ("[7]", "Anthropic. (2024). Claude AI Assistant (UI, Information).",
             "https://claude.ai")
        ]

        for num, text, url in refs:
            st.markdown(f"""
            <div class="ref-item">
                <span class="ref-num">{num}</span>
                <span>{text}<br>
                <a href="{url}" target="_blank" style="color:#7c3aed; font-size:0.82rem;">{url}</a>
                </span>
            </div>
            """, unsafe_allow_html=True)

# ─── Standalone run ───────────────────────────────────────────
if __name__ == "__main__":
    st.set_page_config(
        page_title="Neural Network — ANN",
        page_icon="🧠",
        layout="wide"
    )
    show()
