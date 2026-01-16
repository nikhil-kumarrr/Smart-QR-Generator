import streamlit as st
from qr_generator import generate_qr
from PIL import Image

# Page config
st.set_page_config(
    page_title="Smart QR Generator",
    layout="centered"
)

# ===== Custom CSS =====
st.markdown("""
<style>
/* Full background */
.stApp {
    background: #BDDDFC;
}

/* Center card */
.card {
    background: rgba(255, 255, 255, 0.6);
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    backdrop-filter: blur(8px);
}

/* Title */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    color: #0f172a;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #334155;
    margin-bottom: 25px;
    font-size: 15px;
}

/* Footer */
.footer {
    text-align: center;
    color: #475569;
    font-size: 13px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ===== UI Card =====
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<div class="title">Smart QR Generator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Generate professional, scannable QR codes for URLs</div>',
    unsafe_allow_html=True
)

url = st.text_input(
    "Enter the URL",
    placeholder="https://example.com"
)

generate = st.button("Generate QR", use_container_width=True)

if generate:
    if not url.startswith("http"):
        st.error("Enter a valid URL starting with https://")
    else:
        qr_path = generate_qr(url)
        st.success("QR Generated Successfully")

        img = Image.open(qr_path)
        img = img.resize((230, 230))  # controlled size

        # ---- CENTER ALIGN QR ----
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, caption="Scan this QR")

        with open(qr_path, "rb") as f:
            st.download_button(
                label="Download QR Code",
                data=f,
                file_name="qr_code.png",
                mime="image/png",
                use_container_width=True
            )

st.markdown('</div>', unsafe_allow_html=True)