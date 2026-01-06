import streamlit as st
import tensorflow as tf
from PIL import Image
from utils.vegetation_utils import vegetation_percentage
import streamlit as st
from utils.ui_style import apply_global_style



apply_global_style()

st.markdown("""
<style>
/* ===== TOP NAVBAR ===== */
.navbar {
    background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    margin-bottom: 2rem;
    border-radius: 10px;
}

.navbar-title {
    font-size: 22px;
    font-weight: 900;
    color: #22c55e;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.nav-links a {
    margin-left: 25px;
    text-decoration: none;
    font-size: 15px;
    font-weight: 700;
    color: #e5e7eb;
}

.nav-links a:hover {
    color: #22c55e;
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
        font-size: 14px;
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

st.title("🌿 Vegetation Analysis")

st.markdown("Upload a satellite or land image to analyze vegetation coverage.")

@st.cache_resource
def load_model():
    # Load TensorFlow SavedModel for Keras 3 compatibility
    return tf.saved_model.load("models/vegetation_saved_model")

model = load_model()

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing vegetation..."):
        veg, nonveg, _ = vegetation_percentage(model, image)

    with col2:
        st.markdown("### 📊 Vegetation Statistics")

        st.markdown(f"""
        <div class="metric-card">
            <h2>🌿 {veg}%</h2>
            <p>Vegetation Area</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card" style="margin-top:15px;">
            <h2>🏜️ {nonveg}%</h2>
            <p>Non-Vegetation Area</p>
        </div>
        """, unsafe_allow_html=True)
       

