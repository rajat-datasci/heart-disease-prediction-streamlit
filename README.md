# 🫀 Heart Disease Prediction App (Streamlit)

## 📌 Overview
This project is an end-to-end machine learning application that predicts the risk of heart disease based on user inputs. The model is integrated into an interactive web application built using Streamlit, allowing users to input clinical details and receive instant predictions.

---

## 🎯 Objective
- Build a machine learning model to predict heart disease risk  
- Create an interactive user interface for real-time predictions  
- Demonstrate end-to-end ML workflow including deployment  

---

## 🛠️ Tech Stack
- Language: Python  
- Libraries: Pandas, Seaborn, Scikit-Learn, Joblib, Streamlit  
- Deployment: Streamlit Cloud  

---

## 🔄 Project Workflow

### 1. Data Preparation
- Cleaned and preprocessed dataset  
- Handled inconsistent values and analyzed feature relationships
- Applied encoding for categorical variables  

---

### 2. Model Building
- Trained multiple classification models like Logistic Regression, KNN, Naive Bayes, Decision Tree, SVM. Applied feature scaling selectively based on model requirements.
- Evaluated models using metrics such as Accuracy and F1-Score on training and test data.
- Selected final model (Logistic Regression) for deployment based on Accuracy and F1-Score.  

---

### 3. Model Persistence
- Saved trained model using Joblib  
- Stored preprocessing objects (scaler, feature columns)  

---

### 4. Application Development
- Built an interactive UI using Streamlit  
- Collected user inputs through sliders and dropdowns  

---

### 5. Prediction System
- Scaled input data using saved scaler  
- Passed processed data into trained model  
- Displayed prediction results dynamically  

---

## 🚀 Live Demo
👉 (https://heart-disease-prediction-app-wkmvxrq2udqhsvyzfckqc2.streamlit.app)

## ⚠️ Disclaimer
This application is for educational purposes only and should not be used for medical diagnosis.
