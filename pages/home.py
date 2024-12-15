import streamlit as st
import pandas as pd

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

file_path = "C:/Users/Sekar/Purwadhika/Module Capstone/Module 3/test_data_original.csv"
df = pd.read_csv(file_path)
st.dataframe(df.head())

