
import streamlit as st
import numpy as np
import joblib

# Sayfa başlığı
st.title("Araç Yakıt Tüketimi (MPG) Tahmini")

# Girdi alanları
model_year = st.slider("Model Yılı (1970 - 1982)", 1970, 1982, 1976)
origin_label = st.selectbox("Üretim Bölgesi", ["ABD", "Avrupa", "Japonya"])
origin_mapping = {"ABD": 1, "Avrupa": 2, "Japonya": 3}
origin = origin_mapping[origin_label]
acceleration = st.slider("0-60 mil/saat Hızlanma Süresi (saniye)", 8.0, 24.8, 15.0)

# Normalize edilmiş değerleri kullan
model_year_norm = (model_year - 1970) / (1982 - 1970)
origin_norm = (origin - 1) / (3 - 1)
acceleration_norm = (acceleration - 8.0) / (24.8 - 8.0)

input_data = np.array([[model_year_norm, origin_norm, acceleration_norm]])

# Modeli yükle
model = joblib.load("linear_model.pkl")

# Tahmin
if st.button("Tahmin Et"):
    prediction = model.predict(input_data)
    st.success(f"Tahmini MPG: {prediction[0]:.2f}")
