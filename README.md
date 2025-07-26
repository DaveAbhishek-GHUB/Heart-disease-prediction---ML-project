# Heart Disease Prediction

This repository contains a machine learning model and a Streamlit web application for predicting the likelihood of heart disease based on patient medical data. The project uses a Logistic Regression model trained on a heart disease dataset to provide accurate predictions, which are then deployed via a user-friendly web interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The Heart Disease Prediction project aims to assist medical professionals and individuals in assessing the risk of heart disease using key health metrics. The model is trained on a dataset containing patient information such as age, cholesterol levels, blood pressure, and other clinical features. A Streamlit web application allows users to input their data and receive predictions in real-time.

## Features
- **Predictive Model**: Utilizes a Logistic Regression model for accurate heart disease prediction.
- **Web Interface**: Interactive Streamlit application for easy input and result visualization.
- **Scalable Preprocessing**: Handles one-hot encoding and feature scaling to align user inputs with the trained model.
- **User-Friendly**: Intuitive sliders and dropdowns for entering medical data.
- **Production-Ready**: Deployable model with saved scaler and column configurations.

## Dataset
The dataset used is the [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) (or similar), containing 918 records with 12 features, including:
- **Age**: Patient's age (28–77 years).
- **Sex**: Male (M) or Female (F).
- **ChestPainType**: Type of chest pain (ATA, NAP, ASY, TA).
- **RestingBP**: Resting blood pressure (mmHg).
- **Cholesterol**: Serum cholesterol (mg/dL).
- **FastingBS**: Fasting blood sugar (0 = No, 1 = Yes).
- **RestingECG**: Resting ECG results (Normal, ST, LVH).
- **MaxHR**: Maximum heart rate achieved (60–202 bpm).
- **ExerciseAngina**: Exercise-induced angina (Y = Yes, N = No).
- **Oldpeak**: ST depression induced by exercise.
- **ST_Slope**: Slope of the peak exercise ST segment (Up, Flat, Down).
- **HeartDisease**: Target variable (0 = No disease, 1 = Disease).

The dataset was preprocessed with one-hot encoding for categorical variables and standardized using `StandardScaler`.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Install dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download model files**:
   Ensure the following files are in the project directory:
   - `Logistic_heart.pkl`: Trained Logistic Regression model.
   - `scaler.pkl`: StandardScaler object.
   - `columns.pkl`: List of expected feature columns.

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the Streamlit app in your browser (typically at `http://localhost:8501`).
2. Enter patient details using the provided sliders and dropdowns (e.g., age, sex, cholesterol).
3. Click the **Predict** button to view the prediction:
   - **Green (Success)**: Low risk of heart disease.
   - **Red (Error)**: High risk of heart disease.

## Model Details
- **Algorithm**: Logistic Regression.
- **Performance**:
  - Accuracy: ~86.96%
  - F1 Score: ~88.57%
- **Preprocessing**:
  - Categorical features encoded using one-hot encoding.
  - Numerical features scaled using `StandardScaler`.
- **Training**:
  - Split: 80% training, 20% testing.
  - Random State: 42 for reproducibility.

Other models (KNN, Naive Bayes, Decision Tree, SVM) were evaluated, but Logistic Regression was selected for its balance of performance and interpretability.

## File Structure
```
heart-disease-prediction/
├── Heart.ipynb           # Jupyter notebook for EDA and model training
├── app.py                # Streamlit web application
├── Logistic_heart.pkl    # Trained Logistic Regression model
├── scaler.pkl            # StandardScaler object
├── columns.pkl           # List of feature columns
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

## Dependencies
- Python 3.8+
- pandas
- numpy
- scikit-learn
- streamlit
- joblib
- seaborn (for EDA in notebook)
- matplotlib (for EDA in notebook)

Install all dependencies using:
```bash
pip install pandas numpy scikit-learn streamlit joblib seaborn matplotlib
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows PEP 8 guidelines and includes relevant documentation.