import streamlit as st
from utils.ui_style import apply_global_style


apply_global_style()

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AgroVision AI | About",
    layout="wide"
)

# ================= NAVBAR =================
st.markdown("""
<style>
.navbar {
    background-color: #1e40af;
    padding: 14px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 8px;
    margin-bottom: 30px;
}
.navbar-title {
    font-size: 20px;
    font-weight: 700;
    color: #22c55e;
}
.nav-links a {
    margin-left: 22px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    color: white;
}
.nav-links a:hover {
    text-decoration: underline;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        padding: 1rem;
        gap: 1rem;
    }
    
    .navbar-title {
        font-size: 18px;
        text-align: center;
    }
    
    .nav-links {
        display: flex;
        flex-direction: column;
        width: 100%;
        text-align: center;
    }
    
    .nav-links a {
        margin: 5px 0;
        margin-left: 0;
        font-size: 13px;
    }
}
</style>

<div class="navbar">
    <div class="navbar-title">AGROVISION AI</div>
    <div class="nav-links">
        <a href="/">HOME</a>
        <a href="/Vegetation_Analysis">VEGETATION ANALYSIS</a>
        <a href="/Soil_Detection">SOIL DETECTION</a>
        <a href="/About">ABOUT</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= CONTENT =================

st.title("About AgroVision AI")

st.markdown("""
AgroVision AI is an AI-powered land analysis platform designed to support  
**precision agriculture** and **environmental monitoring**.

The system analyzes images of land and soil to provide clear, visual, and 
data-driven insights into vegetation coverage and soil characteristics. 
This helps farmers, researchers, and decision-makers take informed actions 
without relying on time-consuming manual surveys.
""")

st.subheader("Vegetation Analysis")

st.markdown("""
The vegetation analysis module estimates vegetation and non-vegetation 
coverage from land or satellite images.  
It enables fast assessment of vegetation distribution and helps in 
monitoring crop health and land usage.
""")

st.subheader("Soil Detection")

st.markdown("""
The soil detection module identifies and classifies soil types such as  
**Alluvial, Black, Clay, and Red Soil** from images.  
It provides the dominant soil type along with confidence and coverage 
information to assist in crop planning.
""")

st.markdown("---")

st.markdown(
    "**AgroVision AI simplifies land analysis by delivering fast, accurate, and visual results using AI.**"
)
