import streamlit as st

st.set_page_config(
    page_title="AI Terrorism Data Intelligence Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------- CUSTOM STYLING -----------------------------
st.markdown("""
<style>

/* Overall background */
.stApp {
    background: radial-gradient(circle at top left, #0f172a 0%, #0b1120 60%, #05070d 100%);
}

/* Hide default Streamlit chrome for a cleaner look */
#MainMenu, footer {visibility: hidden;}

/* Header block */
.header-wrap {
    padding: 10px 0 20px 0;
}

.main-title {
    font-size: 46px;
    font-weight: 800;
    background: linear-gradient(90deg, #00c6ff, #7cf7d0 60%, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
}

.subtitle {
    font-size: 18px;
    color: #94a3b8;
    font-weight: 400;
    margin-bottom: 6px;
}

.badge-row {
    display: flex;
    gap: 10px;
    margin: 14px 0 4px 0;
    flex-wrap: wrap;
}

.badge {
    background: rgba(0, 198, 255, 0.08);
    border: 1px solid rgba(0, 198, 255, 0.35);
    color: #7cd8ff;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 500;
}

hr.divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #1f2a3d, transparent);
    margin: 18px 0 28px 0;
}

/* Feature cards */
.card {
    background: linear-gradient(145deg, #131b2c, #0d1420);
    padding: 24px 22px;
    border-radius: 18px;
    margin: 8px 0 18px 0;
    border: 1px solid #1e293b;
    border-left: 4px solid #00c6ff;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    height: 168px;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 28px rgba(0, 198, 255, 0.15);
    border-left: 4px solid #7cf7d0;
}

.card-icon {
    font-size: 30px;
    margin-bottom: 8px;
    display: block;
}

.card h3 {
    color: #f1f5f9;
    font-size: 19px;
    font-weight: 700;
    margin: 0 0 8px 0;
}

.card p {
    color: #94a3b8;
    font-size: 14.5px;
    line-height: 1.5;
    margin: 0;
}

/* Footer info panels */
.info-panel {
    background: linear-gradient(145deg, #10241d, #0d1420);
    border: 1px solid #1c3a2e;
    border-radius: 16px;
    padding: 20px 24px;
    color: #d1fae5;
}

.info-panel h4 {
    color: #7cf7d0;
    margin-top: 0;
}

.cta-panel {
    background: linear-gradient(145deg, #0d2436, #0d1420);
    border: 1px solid #163449;
    border-radius: 16px;
    padding: 18px 24px;
    color: #bfe9ff;
    font-size: 15.5px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------- HEADER -----------------------------
st.markdown('<div class="header-wrap">', unsafe_allow_html=True)
st.markdown('<div class="main-title">🛡️ AI Terrorism Data Intelligence Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Global Terrorism Database Analysis &nbsp;•&nbsp; Trend Forecasting &nbsp;•&nbsp; '
    'Research-Grade Data Insights</div>',
    unsafe_allow_html=True
)
st.markdown("""
<div class="badge-row">
    <span class="badge">📊 Data Analytics</span>
    <span class="badge">🤖 Machine Learning</span>
    <span class="badge">🗺️ Geospatial Visualization</span>
    <span class="badge">📈 Historical Trends</span>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ----------------------------- FEATURE CARDS -----------------------------
cards = [
    ("🌍", "Global Threat Map", "Visualize terrorism incidents across countries using interactive geospatial maps."),
    ("🤖", "Attack Category Prediction", "Predict likely attack categories from historical patterns using ML models."),
    ("🚦", "Risk Level Analysis", "Assess relative risk levels based on attack frequency, casualties, and location."),
    ("🌎", "Country-Wise Analysis", "Explore country-level trends in incidents, fatalities, injuries, and attack types."),
    ("📈", "Trend Forecasting", "Project future incident trends using historical time-series data."),
    ("📊", "Data Explorer", "Filter, browse, analyze, and export records from the Global Terrorism Database."),
]

for row_start in range(0, len(cards), 3):
    cols = st.columns(3)
    for col, (icon, title, desc) in zip(cols, cards[row_start:row_start + 3]):
        with col:
            st.markdown(f"""
            <div class="card">
                <span class="card-icon">{icon}</span>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ----------------------------- FOOTER PANELS -----------------------------
c1, c2 = st.columns([1, 1])
with c1:
    st.markdown("""
    <div class="cta-panel">
        👈 <b>Select a module from the left sidebar</b> to begin exploring the dataset and analysis tools.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-panel">
        <h4>Project Objective</h4>
        This dashboard supports exploratory analysis of the Global Terrorism Database (GTD) for academic
        and research purposes — identifying historical patterns, comparing regional trends, and applying
        data-driven forecasting. It combines <b>data analytics, machine learning, and visualization</b>
        to support research and policy analysis.
    </div>
    """, unsafe_allow_html=True)