import streamlit as st
impot pandas as pd
import joblib

st.set_page_config(
	page_title = "Klasifikasi Tomat",
	page_icon = "🍅"
)

model = joblib.load("model_klasifikasi_tomat.joblib")
scaler = joblib.load("scaler_klasifikasi_tomat.joblib")

st.title("st.title("🍅 Klasifikasi Tomat")
st.markdown("Aplikasi machine learning untuk klasifikasi apakah tomat termasuk kategori **Ekspor, Lokal premium atau Industri**")

berat = st.slider("Berat Tomat", 50, 200, 85)
kekenyalan = s.slider("Tingkat kekenyalan", 3.0, 10.0, 5.0)
kadar_gula = st.slider("Kadar Gula", 2.0, 10.0, 8.0)
tebal_kulit = st.slider("Tebal Kulit", 0.1, 1.0, 0.7)

if st.button("Prediksi"):
	data = pd,DataFrame([[berat, kekenyalan, kadar_gula, tebal_kulit]]	columns=["berat","kekenyalan","kadar_gula","tebal_kulit"])

	data_baru_scaled = scaler.transform(data_baru)
	prediksi = model.predict(data_baru_scaled)[0]
	presentase = max(model.predict_proba(data_baru_scaled)[0])
	st.success(f"Model memprediksi **{prediksi}** dengan keyakinan **{presentase*100:.2f}%**")
	st.balloons()

st.divider()
st.caption("Dibuat dengan 🍅 oleh **saskyaa**")

