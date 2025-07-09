import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("sample_data.csv")
X = df[["temperature", "pressure", "engine_rpm"]]
y = df["code"]

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

st.title("AI-powered Fault Prediction Panel")

st.write("Enter sensor values to predict the fault code:")

temperature = st.number_input("Temperature (°C)", min_value=0, max_value=200, value=135)
pressure = st.number_input("Pressure (bar)", min_value=0.0, max_value=10.0, value=2.2)
engine_rpm = st.number_input("Engine RPM", min_value=0, max_value=5000, value=1900)

if st.button("Predict Fault Code"):
    input_data = pd.DataFrame({
        "temperature": [temperature],
        "pressure": [pressure],
        "engine_rpm": [engine_rpm]
    })
    predicted_code = model.predict(input_data)[0]
    description = df[df["code"] == predicted_code]["description"].values[0]
    probas = model.predict_proba(input_data)
    top_n_idx = probas[0].argsort()[-3:][::-1]
    top_codes = model.classes_[top_n_idx]
    st.success(f"Predicted Fault Code: {predicted_code}")
    st.info(f"Description: {description}")
    st.warning(f"Top 3 probable codes: {', '.join(top_codes)}")

print(df["code"].value_counts())
