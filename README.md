# Telecommunication Customer Churn Prediction

## Project Overview

This repository contains Module 3 and 4 Capstone Projects for the DTI Data Science Program at Purwadhika Digital School. 

This project consists of the following:
- [Customer Churn Prediction Model](#Customer-Churn-Prediction-Model)
- [Customer Churn Prediction App using Streamlit](#Customer-Churn-Prediction-App-using-Streamlit)
- [Model Deployment to Google Cloud](#Model-Deployment-to-Google-Cloud)

## Customer Churn Prediction Model
### Project Files
- `capstone_3.ipynb`  : The notebook containing the end-to-end model development.
- `model.pkl`         : The model saved to a pickle file.
- `data`              : The data folder containing datasets related to this project. The data used for model development is `data_telco_customer_churn.csv`

### Overview


### Evaluation Metrics
The evaluation metrics primarily used in this project are F2 Score, Recall, and ROC AUC Score.

### Modeling Process
- Comparison of multiple classification models without resampling methods
- Comparison of multiple classifcation models with resampling methods
- Choose top 3 models with best F2 score
- Comparison of the top models with hyperparameter tuning
- Choose best model with best F2 score

### Conclusion 
- The best model to predict customer churn is the Gradient Boosting model with Instance Hardness Threshold for the resampling methods.
  

## Customer Churn Prediction App using Streamlit
The streamlit app is available in the `streamlit_app.py` file. The `pages` folder stores the pages related to this app. To run the app, pass this code to your command shell:
```
streamlit run streamlit_app.py
```
Once you've run the file, you can navigate through the app using the sidebar. In the `data` folder of this repository, there are some test data files that you can use to upload a dataset to the app to test the model performance.

## Model Deployment to Google Cloud
The model from this project is uploaded to the Google Cloud Storage and Vertex AI. The following are the files used:
- `deploy.ipynb`    : The notebook containing the deployment process
- `trial_bigq.json` : JSON file containing credentials for authenticating with Google Cloud services, particularly Google BigQuery.
- `dev_trial.json`  : JSON file containing credentials for authenticating with Vertex AI.
