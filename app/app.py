import streamlit as st
import numpy as np
import joblib
import os 

# Loading Model + Scaler Safely 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "models", "loan_default_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))

# UI
st.title("Loan Default Prediction")

Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", [0, 1, 2, 3])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount (in ₹)", min_value=0)
Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", min_value=0)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Encoding
Gender = 1 if Gender == "Male" else 0
Married = 1 if Married == "Yes" else 0
Education = 1 if Education == "Not Graduate" else 0
Self_Employed = 1 if Self_Employed == "Yes" else 0
Property_Area_Semiurban = 1 if Property_Area == "Semiurban" else 0
Property_Area_Urban = 1 if Property_Area == "Urban" else 0
LoanAmount = LoanAmount / 1000

input_data = np.array([[
    Gender, Married, Dependents, Education, Self_Employed,
    ApplicantIncome, CoapplicantIncome, LoanAmount,
    Loan_Amount_Term, Credit_History,
    Property_Area_Semiurban, Property_Area_Urban
]])

input_scaled = scaler.transform(input_data)

if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    if prediction == "Y":
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")