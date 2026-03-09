import streamlit as st

def show():
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

    .section-card {
        background: #fff; border: 1px solid #e5e7eb;
        border-radius: 14px; padding: 24px 28px; margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .section-card h3 {
        color: #0c2340; font-size: 1.05rem; font-weight: 700;
        margin: 0 0 16px 0; padding-bottom: 8px; border-bottom: 2px solid #e0f2fe;
    }
    .section-card p, .section-card li { color: #374151; font-size: 0.93rem; line-height: 1.85; }

    .step-row { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 16px; }
    .step-num {
        background: linear-gradient(135deg, #0284c7, #0369a1);
        color: white; width: 32px; height: 32px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.82rem; font-weight: 700; flex-shrink: 0; margin-top: 2px;
    }
    .step-content strong { color: #0c2340; font-weight: 600; display: block; margin-bottom: 3px; }
    .step-content span   { color: #6b7280; font-size: 0.88rem; line-height: 1.7; }

    .tag-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
    .tag { background:#f0f9ff; border:1px solid #bae6fd; color:#0369a1;
           padding:4px 12px; border-radius:6px; font-size:0.82rem;
           font-family:'IBM Plex Mono',monospace; }
    .tag.red   { background:#fee2e2; border-color:#fca5a5; color:#991b1b; }
    .tag.green { background:#d1fae5; border-color:#6ee7b7; color:#065f46; }
    .tag.gray  { background:#f3f4f6; border-color:#d1d5db; color:#374151; }
    .tag.orange{ background:#fff7ed; border-color:#fed7aa; color:#c2410c; }

    .model-card { border-radius:12px; padding:20px 24px; margin-bottom:12px; }
    .model-svm { background:#eff6ff; border:1px solid #bfdbfe; }
    .model-ann { background:#fdf4ff; border:1px solid #e9d5ff; }
    .model-rf  { background:#f0fdf4; border:1px solid #bbf7d0; }
    .model-ens { background:#fff7ed; border:1px solid #fed7aa; }
    .model-card h4 { font-size:0.98rem; font-weight:700; margin:0 0 8px 0; }
    .model-svm h4 { color:#1d4ed8; } .model-ann h4 { color:#7e22ce; }
    .model-rf h4  { color:#15803d; } .model-ens h4 { color:#c2410c; }
    .model-card p { color:#374151; font-size:0.88rem; line-height:1.75; margin:0; }

    .arch-box {
        background: #0a1628; border-radius: 12px; padding: 24px 28px;
        font-family: 'IBM Plex Mono', monospace;
    }
    .arch-node {
        border-radius: 8px; padding: 8px 16px;
        font-size: 0.82rem; font-weight: 600; text-align: center; min-width: 160px;
    }
    .arch-svm  { background:rgba(96,165,250,0.15); border:1px solid #60a5fa; color:#93c5fd; }
    .arch-ann  { background:rgba(196,181,253,0.15); border:1px solid #c4b5fd; color:#ddd6fe; }
    .arch-rf   { background:rgba(110,231,183,0.15); border:1px solid #6ee7b7; color:#a7f3d0; }
    .arch-vote { background:rgba(251,191,36,0.15);  border:1px solid #fbbf24; color:#fde68a; }
    .arch-out  { background:rgba(248,113,113,0.15); border:1px solid #f87171; color:#fca5a5; }

    .metric-row { display:flex; gap:14px; flex-wrap:wrap; margin-top:14px; }
    .metric-card {
        flex:1; min-width:110px;
        background: linear-gradient(135deg, #0c2340, #1a3a5c);
        border-radius:10px; padding:16px 18px; text-align:center;
    }
    .metric-card .val { color:#7dd3fc; font-size:1.4rem; font-weight:700;
                        font-family:'IBM Plex Mono',monospace; }
    .metric-card .lbl { color:#93c5fd; font-size:0.78rem; margin-top:4px; }

    .ref-item {
        display:flex; gap:10px; padding:10px 0;
        border-bottom:1px solid #f3f4f6;
        color:#374151; font-size:0.88rem; line-height:1.65;
    }
    .ref-num { color:#0284c7; font-weight:700; font-family:'IBM Plex Mono',monospace; min-width:30px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="ml-hero">
        <div class="ml-badge">Model 1 — Machine Learning Ensemble</div>
        <h1>Machine Learning (Ensemble) — Titanic Survival Prediction</h1>
        <p>การพัฒนาโมเดล Ensemble ประกอบด้วย SVM + ANN + Random Forest
        สำหรับทำนายการรอดชีวิตของผู้โดยสารบนเรือ Titanic</p>
    </div>
    """, unsafe_allow_html=True)

    t1, t2, t3, t4, t5 = st.tabs(["📦 Dataset", "🔧 เตรียมข้อมูล", "📐 ทฤษฎี Ensemble", "🏗️ พัฒนาโมเดล", "📚 อ้างอิง"])

    # ── TAB 1: Dataset ────────────────────────────────────────────
    with t1:
        st.markdown("""
        <div class="section-card">
            <h3>📦 ที่มาของ Dataset</h3>
            <p>Dataset ที่ใช้คือ <strong>Titanic — Machine Learning from Disaster</strong>
            ดาวน์โหลดจาก <a href="https://www.kaggle.com/competitions/titanic/data" target="_blank">Kaggle Competition: Titanic</a>
            ประกอบด้วยข้อมูลผู้โดยสารเรือ Titanic จำนวน <strong>891 คน (train set)</strong>
            และ <strong>418 คน (test set)</strong>
            เป้าหมายคือทำนายว่าผู้โดยสารแต่ละคนจะ <strong>รอดชีวิต (1)</strong> หรือ <strong>ไม่รอดชีวิต (0)</strong></p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="section-card">
                <h3>🗂️ Features ของ Dataset</h3>
                <div class="step-row"><div class="step-num">1</div><div class="step-content">
                    <strong>PassengerId</strong><span>รหัสประจำตัวผู้โดยสาร (ใช้เป็น ID เท่านั้น)</span>
                </div></div>
                <div class="step-row"><div class="step-num">2</div><div class="step-content">
                    <strong>Survived</strong><span>Target — 0 = ไม่รอดชีวิต, 1 = รอดชีวิต</span>
                </div></div>
                <div class="step-row"><div class="step-num">3</div><div class="step-content">
                    <strong>Pclass</strong><span>ชั้นโดยสาร — 1 = First, 2 = Second, 3 = Third</span>
                </div></div>
                <div class="step-row"><div class="step-num">4</div><div class="step-content">
                    <strong>Name</strong><span>ชื่อผู้โดยสาร (ใช้ดึง Title เช่น Mr, Mrs, Miss, Master)</span>
                </div></div>
                <div class="step-row"><div class="step-num">5</div><div class="step-content">
                    <strong>Sex</strong><span>เพศ (male / female)</span>
                </div></div>
                <div class="step-row"><div class="step-num">6</div><div class="step-content">
                    <strong>Age</strong><span>อายุผู้โดยสาร (มีค่าหายไปประมาณ 19%)</span>
                </div></div>
                <div class="step-row"><div class="step-num">7</div><div class="step-content">
                    <strong>SibSp / Parch</strong><span>จำนวนพี่น้อง/คู่สมรส และ พ่อแม่/ลูกที่เดินทางด้วย</span>
                </div></div>
                <div class="step-row"><div class="step-num">8</div><div class="step-content">
                    <strong>Ticket / Fare</strong><span>หมายเลขตั๋วและราคาตั๋ว</span>
                </div></div>
                <div class="step-row"><div class="step-num">9</div><div class="step-content">
                    <strong>Cabin</strong><span>หมายเลขห้องโดยสาร (ข้อมูลหายไปมากกว่า 77%)</span>
                </div></div>
                <div class="step-row"><div class="step-num">10</div><div class="step-content">
                    <strong>Embarked</strong><span>ท่าเรือที่ขึ้น — C = Cherbourg, Q = Queenstown, S = Southampton</span>
                </div></div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="section-card">
                <h3>⚠️ ความไม่สมบูรณ์ของข้อมูล</h3>
                <p>Dataset ที่มีปัญหาที่ต้องผ่านกระบวนการเตรียมข้อมูลก่อนนำไปใช้งาน</p>
                <div class="tag-row">
                    <span class="tag red">Age: หายไป ~19% (177 แถว)</span>
                    <span class="tag red">Cabin: หายไป ~77% (687 แถว)</span>
                    <span class="tag red">Embarked: หายไป 2 แถว</span>
                    <span class="tag red">Fare: หายไป 1 แถว (test set)</span>
                    <span class="tag red">Sex/Embarked ยังเป็น String</span>
                    <span class="tag red">ช่วงค่า Features ต่างกันมาก</span>
                    <span class="tag red">FamilySize ไม่มีใน Dataset โดยตรง</span>
                </div>
                <br>
                <p><strong>สัดส่วน Target ใน Train Set:</strong></p>
                <div class="tag-row">
                    <span class="tag green">รอดชีวิต: 342 คน (38.4%)</span>
                    <span class="tag red">ไม่รอดชีวิต: 549 คน (61.6%)</span>
                </div>
                <br>
                <p><strong>Features หลังเตรียมข้อมูล:</strong></p>
                <div class="tag-row">
                    <span class="tag gray">Pclass</span><span class="tag gray">Sex</span>
                    <span class="tag gray">Age → AgeBand</span><span class="tag gray">Fare → FareBand</span>
                    <span class="tag gray">Embarked</span><span class="tag gray">Title</span>
                    <span class="tag gray">FamilySize</span><span class="tag gray">IsAlone</span>
                    <span class="tag gray">HasCabin</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── TAB 2: Data Preparation ───────────────────────────────────
    with t2:
        st.markdown("""
        <div class="section-card">
            <h3>🔧 กระบวนการเตรียมข้อมูล (Data Preparation)</h3>
        </div>
        """, unsafe_allow_html=True)

        steps = [
            ("1", "ดึง Title จากชื่อ (Name → Title)",
             "ดึงคำนำหน้าชื่อ เช่น Mr, Mrs, Miss, Master "
             "แล้วรวม Title ที่หายาก (Dr, Rev, Col ฯลฯ) เป็นกลุ่ม <code>Rare</code> "
             "เพื่อป้องกัน Overfitting"),
            ("2", "สร้าง Feature ครอบครัว",
             "<code>FamilySize = SibSp + Parch + 1</code> — ขนาดครอบครัวรวมตัวเอง<br>"
             "<code>IsAlone = 1</code> หาก FamilySize == 1 เพราะผู้เดินทางคนเดียว "
             "มีอัตราการรอดชีวิตแตกต่างกันอย่างมีนัยสำคัญ"),
            ("3", "เติมค่า Age ที่หายไป",
             "ใช้ค่า Median ของ <code>Age</code> จัดกลุ่มตาม <code>Title × Pclass</code> "
             "เพื่อให้การประมาณอายุแม่นยำกว่า Global Median "
             "จากนั้น Fallback ด้วย Global Median สำหรับกรณีที่ยังหายอยู่"),
            ("4", "เติมค่า Fare และ Embarked ที่หายไป",
             "<code>Fare</code> เติมด้วย Median แยกตาม Pclass — ราคาตั๋วสัมพันธ์กับชั้นโดยสาร<br>"
             "<code>Embarked</code> เติมด้วย Mode (S = Southampton มีสัดส่วนมากที่สุด)"),
            ("5", "Binning Age และ Fare",
             "<code>AgeBand</code> แบ่ง Age เป็น 5 กลุ่ม: เด็ก(0-12), วัยรุ่น(13-18), "
             "ผู้ใหญ่(19-35), กลางคน(36-60), สูงอายุ(60+)<br>"
             "<code>FareBand</code> แบ่ง Fare เป็น 4 Quantile เพื่อลด Outlier"),
            ("6", "Encode Categorical Variables",
             "<code>Sex</code> → female=0, male=1<br>"
             "<code>Embarked</code> → C=0, Q=1, S=2<br>"
             "<code>Title</code> → LabelEncoder (Master=0, Miss=1, Mr=2, Mrs=3, Rare=4)"),
            ("7", "สร้าง HasCabin Indicator",
             "แทนที่จะใช้หมายเลขห้องที่หายไปกว่า 77% สร้าง Binary Feature<br>"
             "<code>HasCabin = 1</code> หากมีข้อมูลห้อง, <code>HasCabin = 0</code> หากไม่มี "
             "เพราะการมีห้องสะท้อนสถานะทางสังคมซึ่งเชื่อมโยงกับโอกาสรอดชีวิต"),
            ("8", "Drop คอลัมน์ที่ไม่จำเป็น",
             "ลบ <code>PassengerId, Name, Ticket, Cabin, SibSp, Parch</code> "
             "เนื่องจากถูกแทนที่ด้วย Feature ใหม่ที่สร้างขึ้นแล้ว"),
            ("9", "Train/Validation Split และ Feature Scaling",
             "แบ่ง 80:20 ด้วย <code>StratifiedKFold</code> เพื่อรักษาสัดส่วน class<br>"
             "Scale ด้วย <code>StandardScaler</code> — fit บน train เท่านั้น "
             "เพื่อป้องกัน Data Leakage"),
        ]

        for num, title, desc in steps:
            st.markdown(f"""
            <div class="section-card" style="padding:16px 22px; margin-bottom:10px;">
                <div class="step-row" style="margin-bottom:0;">
                    <div class="step-num">{num}</div>
                    <div class="step-content">
                        <strong style="font-size:0.97rem;">{title}</strong>
                        <span>{desc}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── TAB 3: Theory ─────────────────────────────────────────────
    with t3:
        st.markdown("""
        <div class="section-card">
            <h3>🧩 Ensemble Learning</h3>
            <p>รวมหลายโมเดลเข้าด้วยกันเพื่อให้ผลทำนายดีกว่าโมเดลเดี่ยว
            โดยมี SVM + ANN + Random Forest
            ซึ่งนำค่าความน่าจะเป็น (Probability) จากทุกโมเดลมาถ่วงน้ำหนักและเฉลี่ยรวม
            จากนั้นเลือกคลาสที่มีค่าสูงสุดเป็นผลลัพธ์</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="section-card">
                <h3>🔵 Support Vector Machine (SVM)</h3>
                <p>SVM หา <strong>Hyperplane</strong> ที่แบ่งข้อมูล 2 คลาสโดยให้
                <strong>Margin</strong> มีค่ามากที่สุด ใช้ <strong>RBF Kernel</strong>
                แปลงข้อมูลไปยัง Feature Space มิติสูง ทำให้แบ่งข้อมูลที่ไม่เป็นเชิงเส้นได้
                มีประสิทธิภาพดีเมื่อ Feature ถูก Scale แล้ว</p>
                <div class="tag-row">
                    <span class="tag">C = 1.0</span><span class="tag">kernel = rbf</span>
                    <span class="tag">gamma = scale</span><span class="tag">probability = True</span>
                </div>
            </div>
            <div class="section-card">
                <h3>🟢 Random Forest</h3>
                <p>Ensemble ของ <strong>Decision Tree</strong> หลายร้อยต้น แต่ละต้น train บน
                <strong>Bootstrap Sample</strong> (Bagging) และแต่ละ Node สุ่มเลือก Feature
                ผลลัพธ์มาจากการโหวตเสียงข้างมาก ทนต่อ Overfitting และ Outlier ได้ดี</p>
                <div class="tag-row">
                    <span class="tag">n_estimators = 300</span><span class="tag">max_depth = 8</span>
                    <span class="tag">max_features = sqrt</span><span class="tag">oob_score = True</span>
                    <span class="tag">class_weight = balanced</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="section-card">
                <h3>🟣 MLP Neural Network (ANN)</h3>
                <p><strong>MLPClassifier</strong> จาก scikit-learn เป็น Feedforward Neural Network
                มี 3 Hidden Layers (128→64→32) ใช้ <strong>ReLU</strong> Activation
                และ <strong>Adam</strong> Optimizer พร้อม <strong>Early Stopping</strong>
                หยุดเมื่อ Validation Loss ไม่ดีขึ้นต่อเนื่อง 20 รอบ</p>
                <div class="tag-row">
                    <span class="tag">layers = (128,64,32)</span><span class="tag">activation = relu</span>
                    <span class="tag">alpha = 0.001</span><span class="tag">early_stopping = True</span>
                    <span class="tag">max_iter = 500</span>
                </div>
            </div>
            <div class="section-card">
                <h3>🟠 Soft Voting Ensemble</h3>
                <p>รวมทั้ง 3 โมเดลด้วย <strong>VotingClassifier (soft)</strong>
                นำ Probability มาถ่วงน้ำหนัก — Random Forest ได้น้ำหนัก <strong>1.5</strong>
                เพราะ OOB Score สูงกว่า SVM และ ANN ซึ่งได้น้ำหนัก <strong>1.0</strong> เท่ากัน</p>
                <div class="tag-row">
                    <span class="tag">SVM weight = 1</span>
                    <span class="tag">ANN weight = 1</span>
                    <span class="tag orange">RF weight = 1.5</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card"><h3>🏛️ ภาพรวมสถาปัตยกรรม Ensemble</h3></div>
        <div class="arch-box">
            <div style="color:#6b7280; font-size:0.78rem; margin-bottom:16px; font-family:'IBM Plex Mono',monospace;">
                Scaled Features → 3 Base Models → Soft Voting → Binary Output
            </div>
            <div style="display:flex; gap:20px; align-items:center; flex-wrap:wrap;">
                <div>
                    <div class="arch-node arch-svm" style="margin-bottom:10px;">🔵 SVM (RBF)<br><span style="font-size:0.7rem;opacity:0.7;">weight = 1.0</span></div>
                    <div class="arch-node arch-ann" style="margin-bottom:10px;">🟣 ANN (128-64-32)<br><span style="font-size:0.7rem;opacity:0.7;">weight = 1.0</span></div>
                    <div class="arch-node arch-rf">🟢 Random Forest (300)<br><span style="font-size:0.7rem;opacity:0.7;">weight = 1.5</span></div>
                </div>
                <div style="color:#4b5563; font-size:1.5rem; font-family:'IBM Plex Mono',monospace;">→</div>
                <div class="arch-node arch-vote" style="padding:20px 24px;">
                    🗳️ Soft Voting<br>
                    <span style="font-size:0.7rem;opacity:0.8;">Weighted Average<br>of Probabilities</span>
                </div>
                <div style="color:#4b5563; font-size:1.5rem; font-family:'IBM Plex Mono',monospace;">→</div>
                <div class="arch-node arch-out" style="padding:20px 24px;">
                    🎯 Survived?<br>
                    <span style="font-size:0.7rem;opacity:0.8;">0 = ไม่รอดชีวิต<br>1 = รอดชีวิต</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── TAB 4: Model Dev ──────────────────────────────────────────
    with t4:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="model-card model-svm"><h4>🔵 SVM</h4>
            <p>Validation Accuracy ≈ 83% | CV (5-fold) ≈ 82%<br>
            ทำงานดีบนข้อมูล Scaled เนื่องจาก SVM sensitive ต่อขนาดข้อมูล</p></div>
            <div class="model-card model-rf"><h4>🟢 Random Forest</h4>
            <p>Validation Accuracy ≈ 84% | OOB Score ≈ 83%<br>
            แข็งแกร่งที่สุดในกลุ่ม จึงได้รับน้ำหนักมากกว่าในการ Voting</p></div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="model-card model-ann"><h4>🟣 ANN (MLP)</h4>
            <p>Validation Accuracy ≈ 82% | CV (5-fold) ≈ 81%<br>
            Early Stopping ช่วยป้องกัน Overfitting บน Dataset ขนาดเล็กได้ดี</p></div>
            <div class="model-card model-ens"><h4>🟠 Ensemble (Soft Voting)</h4>
            <p>Validation Accuracy ≈ 84-85% | ROC-AUC ≈ 0.90<br>
            ผลรวมดีกว่าโมเดลเดี่ยว เพราะแต่ละโมเดลเรียนรู้ Pattern ต่างกัน</p></div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <h3>📈 Metric ที่ใช้วัดผล</h3>
            <div class="metric-row">
                <div class="metric-card"><div class="val">Acc</div><div class="lbl">Accuracy<br>ความถูกต้องรวม</div></div>
                <div class="metric-card"><div class="val">AUC</div><div class="lbl">ROC-AUC<br>แยก Class ได้ดีแค่ไหน</div></div>
                <div class="metric-card"><div class="val">CV</div><div class="lbl">5-Fold Cross Val<br>ความเสถียรโมเดล</div></div>
                <div class="metric-card"><div class="val">OOB</div><div class="lbl">Out-of-Bag<br>สำหรับ Random Forest</div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-card"><h3>💻 Source Code หลัก</h3></div>', unsafe_allow_html=True)
        st.code("""
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

svm_model = SVC(C=1.0, kernel='rbf', gamma='scale', probability=True, random_state=42)

ann_model = MLPClassifier(
    hidden_layer_sizes=(128, 64, 32), activation='relu', solver='adam',
    alpha=0.001, learning_rate='adaptive', max_iter=500,
    early_stopping=True, n_iter_no_change=20, random_state=42
)

rf_model = RandomForestClassifier(
    n_estimators=300, max_depth=8, min_samples_split=4, min_samples_leaf=2,
    max_features='sqrt', oob_score=True, class_weight='balanced', random_state=42
)

ensemble = VotingClassifier(
    estimators=[('svm', svm_model), ('ann', ann_model), ('rf', rf_model)],
    voting='soft',
    weights=[1, 1, 1.5]
)
ensemble.fit(X_train_scaled, y_train)
        """, language="python")

    # ── TAB 5: References ─────────────────────────────────────────
    with t5:
        st.markdown('<div class="section-card"><h3>📚 แหล่งอ้างอิง</h3>', unsafe_allow_html=True)
        refs = [
            ("[1]", "Kaggle. (2012). <em>Titanic — Machine Learning from Disaster</em>.",
             "https://www.kaggle.com/competitions/titanic/data"),
            ("[2]", "Cortes, C., & Vapnik, V. (1995). Support-vector networks. <em>Machine Learning, 20</em>(3), 273–297.",
             "https://link.springer.com/article/10.1007/BF00994018"),
            ("[3]", "Breiman, L. (2001). Random Forests. <em>Machine Learning, 45</em>(1), 5–32.",
             "https://link.springer.com/article/10.1023/A:1010933404324"),
            ("[4]", "Scikit-learn. <em>VotingClassifier Documentation</em>.",
             "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html"),
            ("[5]", "Scikit-learn. <em>MLPClassifier Documentation</em>.",
             "https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html"),
            ("[6]", "Géron, A. (2022). <em>Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow</em> (3rd ed.). O'Reilly.",
             "https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/"),
            ("[7]", "Anthropic. (2024). Claude AI Assistant (UI, Information).",
             "https://claude.ai")
        ]
        for num, text, url in refs:
            st.markdown(f"""
            <div class="ref-item">
                <span class="ref-num">{num}</span>
                <span>{text}<br>
                <a href="{url}" target="_blank" style="color:#0284c7; font-size:0.82rem;">{url}</a></span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(page_title="ML Ensemble — Titanic", page_icon="🚢", layout="wide")
    show()
