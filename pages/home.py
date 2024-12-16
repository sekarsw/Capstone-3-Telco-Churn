import streamlit as st
import pandas as pd
import os

# Header
st.markdown('''
          # Customer Churn Prediction
         
            This is an app that is created to predict customer churn in a telecommunication company 
            using the Gradient Boosting model with Instance Hardness Threshold as the resampling method.
            
            With this app you can:
         - View the model perfomance evaluation with the relevant metrics for this case.
         - Predict customer churn with your own input.
          ''')

st.write('Dataset Preview: ')


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/data_telco_customer_churn.csv")

file_path = os.path.normpath(file_path)

# Original dataset preview
df = pd.read_csv(file_path)

st.dataframe(df.head())

