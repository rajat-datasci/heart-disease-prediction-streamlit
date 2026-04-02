import streamlit as st
import pandas as pd
import joblib

model = joblib.load('logistic_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

# Page config
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="🫀",
    layout="centered"
)

# Header
st.title("🫀 Heart Disease Prediction")
st.markdown("Fill in the details below to assess heart disease risk.")
st.divider()

# Personal Info
st.subheader("Personal Info")
col1, col2 = st.columns(2)
with col1:
    age = st.slider('Age', 18, 100, 40)
with col2:
    sex = st.selectbox('Sex', ['M', 'F'],
                       format_func=lambda x: 'Male' if x == 'M' else 'Female')
st.divider()

# Clinical Measurements
st.subheader("Clinical Measurements")
col1, col2 = st.columns(2)
with col1:
    resting_bp  = st.number_input('Resting Blood Pressure (mm Hg)', 80, 200, 120)
    max_HR      = st.slider('Max Heart Rate', 60, 220, 150)
with col2:
    cholesterol = st.number_input('Cholesterol (mm/dl)', 100, 600, 200)
    old_peak    = st.slider('Old Peak', -2.0, 6.0, 1.0, step=0.1)
st.divider()

# Diagnostic Results
st.subheader("Diagnostic Results")
col1, col2, col3 = st.columns(3)
with col1:
    chest_pain  = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'TA', 'ASY'])
with col2:
    resting_ECG = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
with col3:
    st_slope    = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])

col1, col2 = st.columns(2)
with col1:
    fasting_BS      = st.selectbox('Fasting Blood Sugar > 120 mg/dl',
                                    [0, 1],
                                    format_func=lambda x: 'Yes' if x == 1 else 'No')
with col2:
    exercise_angina = st.selectbox('Exercise Angina', ['Y', 'N'],
                                    format_func=lambda x: 'Yes' if x == 'Y' else 'No')

st.divider()

# Predict Button
if st.button('🔍 Predict Risk', use_container_width=True):
    raw_input = {
        'Age'        : age,
        'RestingBP'  : resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS'  : fasting_BS,
        'MaxHR'      : max_HR,
        'Oldpeak'    : old_peak,
        'Sex_'              + sex             : 1,
        'ChestPainType_'    + chest_pain      : 1,
        'RestingECG_'       + resting_ECG     : 1,
        'ExerciseAngina_'   + exercise_angina : 1,
        'ST_Slope_'         + st_slope        : 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df     = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction   = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error('⚠️ High risk of heart disease detected. Please consult a doctor immediately.')
    else:
        st.success('✅ Low risk of heart disease. Keep maintaining a healthy lifestyle!')