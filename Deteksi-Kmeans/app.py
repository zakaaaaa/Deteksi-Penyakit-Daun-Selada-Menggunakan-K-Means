import streamlit as st
from utils.preprocessing import load_image, resize_image, normalize_rgb
from utils.clustering import apply_kmeans
from utils.visualization import show_image_comparison

st.title("Deteksi Penyakit Tanaman Selada 🥬")

uploaded_file = st.file_uploader("Unggah gambar daun selada", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = load_image(uploaded_file)
    resized = resize_image(image)
    normalized = normalize_rgb(resized)

    segmented, label_map = apply_kmeans(normalized, k=3)

    st.pyplot(show_image_comparison(resized, segmented))

    st.success("Segmentasi selesai. Periksa area yang terindikasi penyakit dari hasil warna yang berbeda.")
