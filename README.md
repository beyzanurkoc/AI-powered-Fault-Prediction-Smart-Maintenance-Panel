# AI-powered Fault Prediction & Smart Maintenance Panel

This project is an interactive Streamlit application that predicts fault codes from sensor data and provides automated maintenance recommendations for armored vehicles.

## Features

* Batch prediction: Analyze thousands or millions of rows from large CSV files, either by uploading directly or specifying a file path (for on-premise/server usage).
* Machine learning-based fault code prediction (Decision Tree Classifier) using sensor data.
* Automated maintenance suggestions for each predicted fault code.
* Model evaluation metrics and confusion matrix for uploaded big data files.
* Professional, readable CSV report downloads with ordered and descriptive columns.
* Simple and user-friendly web interface, suitable for real industry usage.

## Usage Scenarios

* **On-premise/Company Environment :**

  * Users copy large data files (e.g. `bigdata.csv`) directly to the server or shared folder.
  * The panel allows users to specify the full file path and run batch analysis efficiently.

* **Cloud/Demo Usage:**

  * Users can upload CSV files up to 200 MB via the web interface.
  * File path option is not available on Streamlit Cloud for security reasons.

## Getting Started

1. **Clone this repository.**
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit application:**

   ```bash
   streamlit run app.py
   ```
4. **For company/server use:**
   Place your big CSV file (e.g. `bigdata.csv`) in the project directory or a shared folder and enter the full path in the panel.
5. **For cloud/demo use:**
   Upload your data file using the upload option in the web interface.

## File Descriptions

* `app.py`: Main Streamlit application code.
* `sample_data.csv`: Example sensor + fault code dataset (used to train the model).
* `recommendations.csv`: Fault code to maintenance recommendation mapping.
* `requirements.txt`: Required Python packages.
* `.gitignore`: Excludes large files (e.g. `bigdata.csv`) from version control.

## Example Output

After batch prediction, you can download a CSV file with well-ordered and descriptive columns, e.g.:

| Temperature (°C) | Pressure (bar) | Engine RPM | Predicted Fault Code | Maintenance Recommendation           |
| ---------------- | -------------- | ---------- | -------------------- | ------------------------------------ |
| 112              | 2.05           | 1210       | E006                 | Check sensor X and replace if needed |
| 115              | 1.78           | 953        | COOL\_FAN\_ERR       | Check the fan motor and connections  |
| ...              | ...            | ...        | ...                  | ...                                  |

## Live Demo

You can try the app here:
[Open the AI-powered Fault Prediction & Smart Maintenance Panel](https://ai-powered-fault-prediction-smart-maintenance-panel-een6klx26x.streamlit.app/)

> **Note:**
>
> * The file path (server-side) feature works only on company servers or local PC installations.
> * For cloud demo, please use the file upload feature (max 200 MB).

---

**Developed by Beyza Nur Koç**
