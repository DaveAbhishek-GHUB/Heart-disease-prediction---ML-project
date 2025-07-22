import streamlit as st
import pandas as pd
import joblib as jb

model = jb.load("Logistic_heart.pkl")
scaler = jb.load("scaler.pkl")
expected_columns = jb.load("columns.pkl")

st.title("Heart Disease Prediction")
st.markdown("Please enter the following information:")

age = st.slider("Age", min_value=1, max_value=100, value=30)
sex = st.selectbox("Sex", ["F", "M"])  # Use 'M' to match 'Sex_M'
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA"])  # Match model's dummy columns
resting_bp = st.number_input("Resting blood pressure (mmHg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting blood sugar (0 = No, 1 = Yes)", [0, 1])
resting_ecg = st.selectbox("Resting ECG Results", ["Normal", "ST"])  # Only include used dummies
max_heart_rate = st.slider("Maximum heart rate achieved", 60, 200, 150)
exercise_angina = st.selectbox("Exercise induced angina", ["Y", "N"])  # Match 'ExerciseAngina_Y'
oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of peak exercise ST segment", ["Flat", "Up"])  # Match dummy names

if st.button("Predict"):
    # Start with base numeric features
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_heart_rate,
        'Oldpeak': oldpeak,
    }

    # Dynamically add the one-hot encoded features
    raw_input['Sex_' + sex] = 1
    raw_input['ChestPainType_' + chest_pain] = 1
    raw_input['RestingECG_' + resting_ecg] = 1
    raw_input['ExerciseAngina_' + exercise_angina] = 1
    raw_input['ST_Slope_' + slope] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([raw_input])

    # Add any missing columns from training
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Drop label column if present
    if 'HeartDisease' in input_df.columns:
        input_df = input_df.drop(columns=['HeartDisease'])

    # Reorder columns to match model
    input_df = input_df[[col for col in expected_columns if col != 'HeartDisease']]

    # Scale and predict
    input_df = scaler.transform(input_df)
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("You have a high chance of heart disease")
    else:
        st.success("You are safe from heart disease")
