import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# Load model and scaler
model = joblib.load('credit_risk_model.pkl')
scaler = joblib.load('scaler.pkl')

# Function to preprocess user input
def preprocess_input(age, income, emp_length, loan_amount, loan_intent, loan_grade, int_rate, percent_income, credit_hist, home_ownership, cb_default):
    # Create DataFrame with initial order
    data = pd.DataFrame([[
        age, income, emp_length, loan_amount, 
        loan_intent, loan_grade, int_rate, percent_income, 
        credit_hist, home_ownership, cb_default
    ]], columns=[
        'person_age', 'person_income', 'person_emp_length', 'loan_amnt', 
        'loan_intent', 'loan_grade', 'loan_int_rate', 'loan_percent_income', 
        'cb_person_cred_hist_length', 'person_home_ownership', 'cb_person_default_on_file'
    ])
    
    # Reorder columns to match model's expected order
    feature_order = [
        'person_age', 'person_income', 'person_home_ownership', 'person_emp_length',
        'loan_intent', 'loan_grade', 'loan_amnt', 'loan_int_rate',
        'loan_percent_income', 'cb_person_default_on_file',
        'cb_person_cred_hist_length'
    ]
    data = data[feature_order]
    
    # Scale numerical columns
    numerical_cols = [
        'person_age', 'person_income', 'person_emp_length', 'loan_amnt', 
        'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length'
    ]
    data[numerical_cols] = scaler.transform(data[numerical_cols])
    
    return data

# Streamlit app
def main():
    st.title("Credit Risk Assessment")

    st.sidebar.header("User Input Features")

    # User inputs
    age = st.sidebar.slider('Age', 18, 100, 30, help="Enter the applicant's age.")
    income = st.sidebar.number_input('Annual Income', min_value=1000, max_value=1000000, value=50000, step=1000, help="Enter the applicant's annual income.")
    emp_length = st.sidebar.slider('Employment Length (years)', 0, 50, 5, help="Enter the total years of employment.")
    loan_amount = st.sidebar.number_input('Loan Amount', min_value=100, max_value=100000, value=10000, step=100, help="Enter the desired loan amount.")
    loan_intent = st.sidebar.selectbox('Loan Intent', options=['EDUCATION', 'MEDICAL', 'PERSONAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'], index=0, help="Select the purpose of the loan.")
    loan_grade = st.sidebar.selectbox('Loan Grade', options=['A', 'B', 'C', 'D', 'E', 'F', 'G'], index=2, help="Select the loan grade.")
    int_rate = st.sidebar.slider('Interest Rate (%)', 0.0, 40.0, 10.0, step=0.1, help="Enter the loan's interest rate.")
    percent_income = st.sidebar.slider('Loan Percent of Income', 0.01, 1.0, 0.2, step=0.01, help="Enter the loan amount as a percentage of income.")
    credit_hist = st.sidebar.slider('Credit History Length (years)', 1, 30, 5, help="Enter the length of the credit history.")
    home_ownership = st.sidebar.selectbox('Home Ownership', options=['RENT', 'OWN', 'MORTGAGE', 'OTHER'], index=0, help="Select the home ownership status.")
    cb_default = st.sidebar.selectbox('Credit Bureau Default Flag', options=['No', 'Yes'], index=0, help="Indicate if there is a history of default with the credit bureau.")

    # Map categorical inputs to encoded values
    loan_intent_mapping = {'EDUCATION': 0, 'MEDICAL': 1, 'PERSONAL': 2, 'VENTURE': 3, 'HOMEIMPROVEMENT': 4, 'DEBTCONSOLIDATION': 5}
    loan_grade_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    home_ownership_mapping = {'RENT': 0, 'OWN': 1, 'MORTGAGE': 2, 'OTHER': 3}
    cb_default_mapping = {'No': 0, 'Yes': 1}

    # Preprocess inputs
    processed_data = preprocess_input(
        age, income, emp_length, loan_amount,
        loan_intent_mapping[loan_intent], loan_grade_mapping[loan_grade],
        int_rate, percent_income, credit_hist,
        home_ownership_mapping[home_ownership], cb_default_mapping[cb_default]
    )

    # Debugging feature names
    print("Input Data Features:", processed_data.columns.tolist())
    print("Model Features:", model.feature_names_in_)

    if st.button("Predict Credit Risk"):
        prediction = model.predict(processed_data)
        risk_score = model.predict_proba(processed_data)[0][1]

        st.subheader("Risk Score")
        st.progress(int(risk_score * 100))

        if prediction[0] == 1:
            st.error(f"High Credit Risk! Risk Score: {risk_score:.2f}")
        else:
            st.success(f"Low Credit Risk! Risk Score: {risk_score:.2f}")

    # SHAP explanation
    if st.button("Explain Prediction"):
        explainer = shap.Explainer(model)
        shap_values = explainer(processed_data)
        st.subheader("SHAP Explanation")
    
        # Create a Matplotlib figure for SHAP summary plot
        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, processed_data, show=False)  # Disable direct display
        st.pyplot(fig)  # Pass the figure explicitly

if __name__ == '__main__':
    main()
