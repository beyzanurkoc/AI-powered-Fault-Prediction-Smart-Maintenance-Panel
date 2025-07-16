import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import random


st.title("AI Fault Code Prediction and Maintenance Suggestion Panel")

tab1, tab2, tab3 = st.tabs(["Prediction", "Model Evaluation", "Visualizations"])


df = pd.read_csv("sample_data.csv")
X = df[["temperature", "pressure", "engine_rpm"]]
y = df["code"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

recommendations = pd.read_csv("recommendations.csv")
suggestion_map = dict(zip(recommendations["code"], recommendations["recommendation"]))


with tab1:
    st.header("Predict Fault Code")
    st.info("Please enter the latest sensor values OR click the button to get simulated live data!")

    if st.button("Get Live Sensor Data"):
        temperature = random.randint(60, 120)
        pressure = round(random.uniform(1.0, 3.0), 2)
        engine_rpm = random.randint(900, 1400)
        st.session_state["temperature"] = temperature
        st.session_state["pressure"] = pressure
        st.session_state["engine_rpm"] = engine_rpm
    else:
        temperature = st.session_state.get("temperature", 80)
        pressure = st.session_state.get("pressure", 2.0)
        engine_rpm = st.session_state.get("engine_rpm", 1000)

    temperature = st.number_input("Temperature (°C)", min_value=0, max_value=200, value=temperature, key="temp_input_1")
    pressure = st.number_input("Pressure (bar)", min_value=0.0, max_value=10.0, value=pressure, key="press_input_1")
    engine_rpm = st.number_input("Engine RPM", min_value=0, max_value=5000, value=engine_rpm, key="rpm_input_1")

    if st.button("Predict Fault Code", key="predict_button_1"):
        sample_input = pd.DataFrame({
            "temperature": [temperature],
            "pressure": [pressure],
            "engine_rpm": [engine_rpm]
        })
        predicted_code = model.predict(sample_input)[0]
        st.success(f"Predicted fault code: {predicted_code}")

        suggestion = suggestion_map.get(predicted_code, "No recommendation available.")
        st.info(f"Suggested maintenance: {suggestion}")


with tab2:
    st.header("Model Evaluation")
    st.warning("Here you can view the model's performance metrics, such as accuracy, F1-score, and the detailed classification report. You can also see the confusion matrix showing how well the model distinguishes between fault codes.")
    y_pred = model.predict(X_test)
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report_dict).transpose()

    accuracy = report_dict["accuracy"]
    f1_macro = report_df.loc["macro avg", "f1-score"]

    st.metric(label="Accuracy", value=f"{accuracy:.2f}")
    st.metric(label="Macro F1-score", value=f"{f1_macro:.2f}")
    st.subheader("Classification Report ")
    st.dataframe(report_df.round(2))

    st.subheader("Confusion Matrix ")
    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    fig, ax = plt.subplots(figsize=(8, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(ax=ax, xticks_rotation=90)
    st.pyplot(fig)

with tab3:
    st.header("Feature Importance ")
    st.info("The feature importance graph below shows which sensor values have the most influence on the model's fault code prediction.")
    feature_names = ["temperature", "pressure", "engine_rpm"]
    importances = model.feature_importances_
    fig2, ax2 = plt.subplots()
    ax2.bar(feature_names, importances)
    ax2.set_ylabel("Importance")
    ax2.set_title("Feature Importance")
    st.pyplot(fig2)
