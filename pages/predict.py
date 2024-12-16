import streamlit as st
import os
import pandas as pd
import numpy as np

# Load model (replace 'model.pkl' with the path to your trained model)
import pickle

pickle_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../model.pkl")
pickle_file_path = os.path.normpath(pickle_file_path)

with open(pickle_file_path, 'rb') as file:
    model = pickle.load(file)

# User input function
def user_input(prefix=""):

    
    dependents = st.selectbox('Dependents', ('Yes', 'No'), key=f'{prefix}dependents')
    tenure = st.slider('Tenure (months)', 0, 72, key=f'{prefix}tenure')
    internet_service = st.selectbox('Internet Service', ('DSL', 'Fiber optic', 'No'), key=f'{prefix}internet_service')

    # If internet_service is "No", automatically set related fields and disable them
    if internet_service == "No":
        online_security = st.selectbox('Online Security', ('No internet service',), key=f'{prefix}online_security', disabled=True)
        online_backup = st.selectbox('Online Backup', ('No internet service',), key=f'{prefix}online_backup', disabled=True)
        device_protection = st.selectbox('Device Protection', ('No internet service',), key=f'{prefix}device_protection', disabled=True)
        tech_support = st.selectbox('Tech Support', ('No internet service',), key=f'{prefix}tech_support', disabled=True)
    else:
        # Otherwise, show all options normally
        online_security = st.selectbox('Online Security', ('No', 'Yes'), key=f'{prefix}online_security')
        online_backup = st.selectbox('Online Backup', ('No', 'Yes'), key=f'{prefix}online_backup')
        device_protection = st.selectbox('Device Protection', ('No', 'Yes'), key=f'{prefix}device_protection')
        tech_support = st.selectbox('Tech Support', ('No', 'Yes'), key=f'{prefix}tech_support')
    contract = st.selectbox('Contract', ('Month-to-month', 'Two year', 'One year'), key=f'{prefix}contract')
    billing = st.selectbox('Paperless Billing', ('Yes', 'No'), key=f'{prefix}billing')
    charges = st.slider('Monthly Charges', 18.8, 118.65, key=f'{prefix}charges')
    
    data = {
        'Dependents': dependents,
        'tenure': tenure,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'InternetService': internet_service,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'Contract': contract,
        'PaperlessBilling': billing,
        'MonthlyCharges': charges
    }
    data_df = pd.DataFrame(data, index=[0])

    return data_df

# Page design
st.sidebar.title("Churn Prediction Options")
prediction_type = st.sidebar.radio("Choose input type:", ["Single Data", "Multiple Data"])

if prediction_type == "Single Data":
    st.header("Single Data Prediction")

    col1, col2 = st.columns([1, 2])

    # User input
    with col1:
        st.subheader("User Input")
        df = user_input(prefix="single_")
        predict_button = st.button("Predict")

    with col2:
        st.subheader('Data Preview')
        st.dataframe(df)

        st.subheader("Prediction")
        if predict_button:
            prediction = model.predict(df)
            st.success(f"Prediction: {'Churn' if prediction == 1 else 'No Churn'}")

elif prediction_type == "Multiple Data":
    st.header("Multiple Data Prediction")

    col1, col2 = st.columns([1, 2])

    # User input and data preview
    with col1:
        st.subheader("User Input")
        df = user_input(prefix="multi_")

        add_button = st.button("Add Data")
        clear_button = st.button("Clear All Data")

        if "multi_data" not in st.session_state:
            st.session_state.multi_data = pd.DataFrame(columns=df.columns)  # Initialize with correct columns

        if add_button:
            st.session_state.multi_data = pd.concat([st.session_state.multi_data, df], ignore_index=True)
            # Rerun the script by changing the query parameters
            st.experimental_set_query_params(data_updated=True)

        if clear_button:
            st.session_state.multi_data = pd.DataFrame(columns=df.columns)  # Reset DataFrame
            st.experimental_set_query_params(data_updated=True)

        predict_button = st.button("Predict")

    with col2:
        st.subheader("Dataframe Preview")
        st.dataframe(st.session_state.multi_data)

        # Prediction
        st.subheader("Prediction")

        if predict_button and not st.session_state.multi_data.empty:
            input_data = st.session_state.multi_data
            predictions = model.predict(input_data)
            st.session_state.multi_data["Prediction"] = ["Churn" if pred == 1 else "No Churn" for pred in predictions]
            st.dataframe(st.session_state.multi_data)
