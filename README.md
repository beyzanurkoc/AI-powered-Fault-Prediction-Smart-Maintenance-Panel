# AI-powered Fault Prediction & Smart Maintenance Panel

This project is an interactive Streamlit web application for predicting fault codes and providing smart maintenance recommendations for armored vehicles.

## Features

- Machine learning model (Decision Tree) predicts fault codes based on sensor inputs
- Maintenance recommendations for each predicted fault code (automatic suggestion system)
- Supports manual input and simulated live data
- Batch prediction: Upload large CSV files to automatically analyze and generate predictions for thousands of rows
- Visualizes model evaluation metrics, confusion matrix, and feature importance
- Downloadable results and summary statistics

## Getting Started

1. **Clone or download** this repository.
2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
3. **Run the Streamlit panel:**
    ```
    streamlit run app.py
    ```

## File Descriptions

- `app.py`: Main Streamlit application
- `sample_data.csv`: Sample sensor and fault code dataset (for model training)
- `recommendations.csv`: Maintenance suggestions for each fault code
- `requirements.txt`: Python package requirements
- `.gitignore`: Excludes large files (e.g., `bigdata.csv`) from version control

## Usage

- **Manual/Live Prediction:** Enter sensor values manually or simulate live data to predict fault codes and receive maintenance suggestions.
- **Batch Prediction:** Upload a CSV file containing thousands of sensor readings (e.g., `bigdata.csv`). The system will predict fault codes and generate maintenance recommendations for all rows automatically.  
  *Note: For performance and version control reasons, do not upload extremely large CSV files (over 100 MB) to this repository.*

- **Visualizations:** View model performance metrics, confusion matrix, and feature importance charts.
- **Download Results:** Download prediction results as a CSV file for further analysis.

## Live Demo

You can try the app live here: [Open the Smart Maintenance Panel](https://ai-powered-fault-prediction-smart-maintenance-panel-een6klx26x.streamlit.app/)


---

Developed by Beyza Nur Koç
