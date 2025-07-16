# AI-powered Fault Prediction & Smart Maintenance Panel

This project is an interactive Streamlit web application for predicting fault codes and providing smart maintenance recommendations for armored vehicles. The project was developed as part of a 20-day internship assignment at FNSS.

## Features

- Machine learning model (Decision Tree) predicts fault codes based on sensor inputs
- Maintenance recommendations for each predicted fault code (automatic suggestion system)
- Supports manual input and simulated live data
- Visualizes model evaluation metrics, confusion matrix, and feature importance

## Getting Started

1. Clone or download this repository.
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the Streamlit panel:
    ```
    streamlit run app.py
    ```

## File Descriptions

- `app.py`: Main Streamlit panel
- `sample_data.csv`: Sample sensor and fault code data
- `recommendations.csv`: Maintenance suggestions for each code
- `requirements.txt`: Python package requirements


---

Developed by Beyza Nur Koç, FNSS Summer Internship 2025.
