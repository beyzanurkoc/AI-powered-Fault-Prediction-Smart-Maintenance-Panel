import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

st.title("AI Fault Code Prediction")

df = pd.read_csv("sample_data.csv")

X = df[["temperature", "pressure", "engine_rpm"]]
y = df["code"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Classification report
from sklearn.metrics import classification_report
report_dict = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report_dict).transpose()
accuracy = report_dict["accuracy"]
f1_macro = report_df.loc["macro avg", "f1-score"]
st.metric(label="Accuracy", value=f"{accuracy:.2f}")
st.metric(label="Macro F1-score", value=f"{f1_macro:.2f}")
st.subheader("Classification Report (Tablo)")
st.dataframe(report_df.round(2))

# BAKIM ÖNERİSİ
recommendations = pd.read_csv("recommendations.csv")
suggestion_map = dict(zip(recommendations["code"], recommendations["recommendation"]))

# Kullanıcıdan veri al
st.subheader("Predict Fault Code with Your Inputs")
temperature = st.number_input("Temperature (°C)", min_value=0, max_value=200, value=80)
pressure = st.number_input("Pressure (bar)", min_value=0.0, max_value=10.0, value=2.0)
engine_rpm = st.number_input("Engine RPM", min_value=0, max_value=5000, value=1000)

if st.button("Predict Fault Code"):
    sample_input = pd.DataFrame({
        "temperature": [temperature],
        "pressure": [pressure],
        "engine_rpm": [engine_rpm]
    })
    predicted_code = model.predict(sample_input)[0]
    st.success(f"Predicted fault code: {predicted_code}")

    suggestion = suggestion_map.get(predicted_code, "No recommendation available.")
    st.info(f"Suggested maintenance: {suggestion}")
