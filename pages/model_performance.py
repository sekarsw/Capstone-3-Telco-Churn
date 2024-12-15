import streamlit as st
import time
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import fbeta_score, recall_score, roc_auc_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay

# Load model
pickle_file_path = "model.pkl"

with open(pickle_file_path, 'rb') as file:
    model = pickle.load(file)

st.header('Model Performance')

st.write('''
         This app has a predefined dataset to evaluate model performance. You can use your own dataset by uploading it in the **Dataset Selection** on the sidebar.
         Make sure your dataset has the 'Churn' label if you choose to upload your own.
         ''')

# Initialize session state for progress bar and threshold
if "progress_complete" not in st.session_state:
    st.session_state["progress_complete"] = False

if "threshold" not in st.session_state:
    st.session_state["threshold"] = 0.5

# Sidebar Dataset Selection
side_bar = st.sidebar.title('Dataset Selection')
dataset_option = st.sidebar.radio(
    "Choose dataset:", ["Default Dataset", "Upload Your Own Dataset"]
)

if dataset_option == "Default Dataset":
    # Load original test dataset
    df_test = pd.read_csv('test_data_original.csv')
    X_test = df_test.drop(columns=['Churn'])
    y_test = df_test['Churn']
else:
    uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV format):", type="csv")
    if uploaded_file is not None and not st.session_state["progress_complete"]:
        # Show progress bar only once
        progress_bar = st.sidebar.progress(0)
        for pct_complete in range(100):
            time.sleep(0.05)
            progress_bar.progress(pct_complete + 1)
        st.sidebar.success('Dataset uploaded successfully!')
        st.session_state["progress_complete"] = True

        # Read uploaded file
        df_test = pd.read_csv(uploaded_file)
        st.write("Uploaded Dataset Preview:")
        st.dataframe(df_test.head())

        X_test = df_test.drop(columns=['Churn'])
        y_test = df_test['Churn']
    elif uploaded_file is None:
        st.sidebar.warning("Please upload a dataset to proceed.")
        st.stop()
    else:
        # Dataset already processed, skip progress bar
        df_test = pd.read_csv(uploaded_file)
        X_test = df_test.drop(columns=['Churn'])
        y_test = df_test['Churn']

# Predict probabilities and labels
y_proba = model.predict_proba(X_test)[:, 1]

# Slider for threshold adjustment
st.subheader("Threshold Adjustment")

# Reset threshold button
reset_button = st.button("Reset Threshold to 0.5")
if reset_button:
    st.session_state["threshold"] = 0.5

threshold = st.slider(
    "Select prediction threshold:", 
    0.0, 1.0, st.session_state["threshold"], 0.01
)
st.session_state["threshold"] = threshold

# Adjust predictions based on threshold
y_pred = (y_proba >= threshold).astype(int)

# Metrics Calculation
f2 = fbeta_score(y_test, y_pred, beta=2)
recall = recall_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_proba)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Financial Savings Calculation 
# Result of model prediction
tn, fp, fn, tp = cm.ravel()
# Average Revenue
avg_revenue = df_test['MonthlyCharges'].mean()
# Average Customer Lifespan
avg_lifespan = df_test['tenure'].mean()
# CLV 
clv = avg_revenue * avg_lifespan
# CAC
cac = 300
# CRC
crc = 60

# Cost Calculation
total_cust = sum([tn, fp, fn, fp])
total_revenue = total_cust * clv
crc_after = (tp + fp) * crc
cac_after = fn * cac
total_after = crc_after + cac_after

# Revenue Loss
loss_after = fn * clv

# Net Revenue
net_revenue_after = total_revenue - (total_after + loss_after)

# Display UI

# Display Metrics
st.subheader("Model Performance Metrics")
col1, col2, col3 = st.columns(3)
col1.metric(label='F2 Score', value=f'{f2:.2f}')
col2.metric(label='Recall Score', value=f'{recall:.2f}')
col3.metric(label='ROC AUC Score', value=f'{roc_auc:.2f}')

# Financial Savings
st.subheader("Net Revenue and Total Cost")
col_revenue, col_cost = st.columns(2)
col_revenue.metric(label='Net Revenue', value=f'${net_revenue_after:,.2f}')
col_cost.metric(label='Total Cost', value=f'${total_after:,.2f}')



col_cm, col_roc = st.columns(2)
# Display Confusion Matrix
col_cm.subheader("Confusion Matrix")
col_cm.write(' ')
fig, ax = plt.subplots(figsize=(6, 4))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(ax=ax, cmap="Reds")
col_cm.pyplot(fig)

# ROC Curve
col_roc.subheader("ROC Curve")
fig, ax = plt.subplots(figsize=(3, 3))
roc_disp = RocCurveDisplay.from_predictions(y_test, y_proba, ax=ax)
col_roc.pyplot(fig)


