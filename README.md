# Loan Default Prediction

A machine learning project that predicts whether a loan application will be approved or not, based on applicant details such as income, credit history, education, and property area.

---

## Project Structure

loan-default-prediction/
│
├── data/
│   ├── raw/
│   │   ├── train.csv
│   │   └── test.csv
│
├── notebooks/
│   └── loan_prediction.ipynb
│
├── models/
│   ├── loan_default_model.pkl
│   └── scaler.pkl
│
├── app/
│   └── app.py
│
└── requirements.txt

---

## Business Impact

Loan default is one of the biggest financial risks for banks and NBFCs in India. 
According to RBI reports, bad loans (NPAs) have cost Indian banks over ₹10 lakh crore in losses over the past decade.

This project directly addresses that problem:

| Business Metric | Impact |
|---|---|
| **Faster Decisions** | Manual review takes days — this model predicts in seconds |
| **Reduced Default Risk** | Credit History + Income based filtering reduces bad loan approvals |
| **Cost Saving** | Automating screening reduces dependency on manual underwriters |
| **Consistency** | Model applies same logic to every application — no human bias |
| **Scalability** | Can process thousands of applications simultaneously |

> Even a 1% reduction in loan defaults can save a mid-sized bank crores of rupees annually.

---

## Problem Statement

Financial institutions receive thousands of loan applications every day. Manually reviewing each application is time-consuming and error-prone. This project automates the loan approval decision using machine learning — helping banks and NBFCs make faster and more consistent decisions.

---

## Dataset

- **Source:** Kaggle — Loan Prediction Dataset

Download from Kaggle: [Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)

After downloading, place files here:
```
data/raw/train.csv
data/raw/test.csv
```

- **Train size:** 614 rows, 13 columns
- **Target column:** `Loan_Status` (Y = Approved, N = Not Approved)

**Features used:**

| Feature | Description |
|---|---|
| Gender | Applicant's gender |
| Married | Applicant's marital status |
| Dependents | Number of dependents |
| Education | Graduate or Not Graduate |
| Self_Employed | Self employed or salaried |
| ApplicantIncome | Monthly income of applicant |
| CoapplicantIncome | Monthly income of co-applicant |
| LoanAmount | Loan amount requested (in thousands) |
| Loan_Amount_Term | Loan repayment term in days |
| Credit_History | Past credit repayment record |
| Property_Area | Rural, Semiurban, or Urban |

---

## ML Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Missing Value Handling
4. Feature Engineering (Label Encoding + One-Hot Encoding)
5. Train-Test Split (80-20)
6. Feature Scaling (StandardScaler)
7. Model Training (Logistic Regression, Decision Tree, Random Forest)
8. Model Evaluation (Accuracy, Classification Report, Confusion Matrix)
9. Model Saving (joblib)
10. Streamlit Deployment

---

## Models Trained

| Model | Result |
|---|---|
| Logistic Regression | Best Accuracy |
| Decision Tree | Trained & Evaluated |
| Random Forest | Trained & Evaluated |

Logistic Regression performed best and was selected as the final model.

---

## Key Findings

- **Credit History** is the most influential factor in loan approval
- Applicants with higher income and lower loan amount have better approval chances
- Married applicants and graduates have slightly higher approval rates
- Semiurban property area showed highest approval rate in the dataset

---

## How to Run

**1. Clone the repository**

git clone https://github.com/md-faiyazkhan/loan-default-prediction.git
cd loan-default-prediction

**2. Install dependencies**
pip install -r requirements.txt

**3. Run the Streamlit app**
streamlit run app/app.py

---

## Requirements

pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
streamlit

---

## Skills Demonstrated

- Data Cleaning & Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Binary Classification
- Model Evaluation
- Web App Deployment using Streamlit

---

## Author

**Your Name**  
Self-taught ML Engineer | IIT Patna Certified (AI & ML — Intellipaat)  
[LinkedIn](https://linkedin.com/in/mdfaiyazkhan) | [GitHub](https://github.com/md-faiyazkhan)