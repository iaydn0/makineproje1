
import streamlit as st
import numpy as np
import joblib

# Sayfa başlığı
st.title("Araç Yakıt Tüketimi (MPG) Tahmini")

# Girdi alanları
model_year = st.slider("Model Yılı", 70, 82, 76)
origin = st.selectbox("Üretim Bölgesi", [1, 2, 3])
acceleration = st.slider("Hızlanma (0-60 mil/sn)", 8.0, 24.8, 15.0)

# Normalize edilmiş değerleri kullan
model_year_norm = (model_year - 70) / (82 - 70)
origin_norm = (origin - 1) / (3 - 1)
acceleration_norm = (acceleration - 8.0) / (24.8 - 8.0)

input_data = np.array([[model_year_norm, origin_norm, acceleration_norm]])

# Modeli yükle
model = joblib.load("linear_model.pkl")

# Tahmin
if st.button("Tahmin Et"):
    prediction = model.predict(input_data)
    st.success(f"Tahmini MPG: {prediction[0]:.2f}")
