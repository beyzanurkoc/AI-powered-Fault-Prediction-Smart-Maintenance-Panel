import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

st.title("AI Fault Code Prediction and Maintenance Suggestion Panel")

sample_df = pd.read_csv("sample_data.csv")
X = sample_df[["temperature", "pressure", "engine_rpm"]]
y = sample_df["code"]
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

recommendations = pd.read_csv("recommendations.csv")
recommendation_map = dict(zip(recommendations["code"], recommendations["recommendation"]))

tab1, tab2, tab3 = st.tabs(["Batch Prediction", "Model Evaluation", "Visualizations"])

with tab1:
    st.header("Batch Prediction ")

    st.subheader("Option 1: Upload CSV file (max 200MB)")
    uploaded_file = st.file_uploader("Upload your big CSV file", type=["csv"], key="batch_csv")

    st.subheader("Option 2: Load from server path")
    file_path = st.text_input("Or enter the full path to your CSV file (e.g. C:/proje/bigdata.csv):")

    bigdata = None

    if file_path:
        try:
            bigdata = pd.read_csv(file_path)
            st.success(f"File loaded from: {file_path}")
        except Exception as e:
            st.error(f"Could not read file from path: {e}")

    elif uploaded_file is not None:
        bigdata = pd.read_csv(uploaded_file)
        st.success("File loaded from upload!")

    if bigdata is not None:
        st.write("Sample of loaded data:")
        st.dataframe(bigdata.head(20))

        X_big = bigdata[["temperature", "pressure", "engine_rpm"]]
        bigdata["predicted_code"] = model.predict(X_big)
        bigdata["recommendation"] = bigdata["predicted_code"].map(recommendation_map)

        st.session_state["uploaded_bigdata"] = bigdata

        st.success("Predictions completed!")
        st.dataframe(bigdata.head(20))

        csv = bigdata.to_csv(index=False).encode()
        st.download_button("Download Results as CSV", data=csv, file_name="bigdata_with_predictions.csv", mime="text/csv")
    else:
        st.info("Please upload a CSV file **or** enter a valid file path (absolute path) to your big data CSV file.")
        st.session_state["uploaded_bigdata"] = None

with tab2:
    st.header("Model Evaluation on Uploaded Data")
    bigdata = st.session_state.get("uploaded_bigdata", None)
    if bigdata is not None:
        if "code" in bigdata.columns:
            y_true = bigdata["code"]
            y_pred = bigdata["predicted_code"]
            st.write("Evaluating using the actual 'code' column in the uploaded file.")
        else:
            y_true = None
            y_pred = bigdata["predicted_code"]
            st.write("No true fault codes in uploaded file. Evaluation will only show predicted distribution.")

        st.subheader("Predicted Fault Code Distribution")
        st.bar_chart(bigdata["predicted_code"].value_counts())

        if y_true is not None:
            st.subheader("Classification Report")
            report_dict = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
            report_df = pd.DataFrame(report_dict).transpose()
            st.dataframe(report_df.round(2))

            st.subheader("Confusion Matrix")
            labels = sorted(list(set(y_true) | set(y_pred)))
            cm = confusion_matrix(y_true, y_pred, labels=labels)
            fig, ax = plt.subplots(figsize=(8, 6))
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
            disp.plot(ax=ax, xticks_rotation=90)
            st.pyplot(fig)
        else:
            st.info("True codes ('code' column) not found in uploaded file. Showing only predicted code distribution.")
    else:
        st.warning("Please upload a big data CSV file in the Batch Prediction tab first!")

with tab3:
    st.header("Feature Importance")
    st.info("The feature importance graph below shows which sensor values have the most influence on the model's fault code prediction.")
    feature_names = ["temperature", "pressure", "engine_rpm"]
    importances = model.feature_importances_
    fig2, ax2 = plt.subplots()
    ax2.bar(feature_names, importances)
    ax2.set_ylabel("Importance")
    ax2.set_title("Feature Importance")
    st.pyplot(fig2)
