# Telecommunication Customer Churn Prediction

## Project Overview

This repository contains Module 3 and 4 Capstone Projects for the DTI Data Science Program at Purwadhika Digital School. 

This project consists of the following:
- [Customer Churn Prediction Model](#Customer-Churn-Prediction-Model)
- [Customer Churn Prediction App using Streamlit](#Customer-Churn-Prediction-App-using-Streamlit)
- [Model Deployment to Google Cloud](#Model-Deployment-to-Google-Cloud)

## Customer Churn Prediction Model
### Project Files
- [`Capstone 3 - Telco Churn.ipynb`](https://github.com/sekarsw/Capstone-3-Telco-Churn/blob/main/Capstone%203%20-%20Telco%20Churn.ipynb)  : The notebook containing the end-to-end model development.
- `model.pkl`         : The model saved to a pickle file.
- [`data`](https://github.com/sekarsw/Capstone-3-Telco-Churn/tree/main/data)              : The data folder containing datasets related to this project. The data used for model development is `data_telco_customer_churn.csv`

### Overview


### Evaluation Metrics
The evaluation metrics primarily used in this project are F2 Score, Recall, and ROC AUC Score. The F2 Score gives balance between Precision and Recall, with more emphasis on Recall. Both the F2 Score and Recall tells us how well the model minimizes the False Negatives, which are the customer incorrectly predicted to not churn but actually churns. The ROC AUC score 

### Modeling Process
- Comparison of multiple classification models without resampling methods
  - Evaluate based on F2 score, filter models with F2 score above 0.5 for either train or test result.
- Comparison of multiple classification models with resampling methods
  - Evaluate based on standard deviation of Cross Validation, F2, Recall, ROC AUC.
  - Choose the 3 best models with the smallest F2 score difference from train and test result.
- Comparison of the top models with hyperparameter tuning
  - AdaBoost with Instance Hardness Threshold
  - Gradient Boosting with Instance Hardness Threshold
  - Logistic Regression with Instance Hardness Threshold

### Result

- The best model to predict customer churn is the Gradient Boosting model with Instance Hardness Threshold for the resampling methods.
  

## Customer Churn Prediction App using Streamlit
The streamlit app is available in the [`streamlit_app.py`](https://github.com/sekarsw/Capstone-3-Telco-Churn/blob/main/streamlit_app.py) file. The `pages` folder stores the pages related to this app. To run the app, pass this code to your command shell:

```
streamlit run streamlit_app.py
```

Once you've run the file, you can navigate through the app using the sidebar. 

In the `data` folder of this repository, there are some test data files that you can use to upload a dataset to the app to test the model performance.

## Model Deployment to Google Cloud
The model from this project is uploaded to the Google Cloud Storage and Vertex AI. The following are the files used:
- [`deploy.ipynb`](https://github.com/sekarsw/Capstone-3-Telco-Churn/blob/main/deploy.ipynb)    : The notebook containing the deployment process
- `trial_bigq.json` : JSON file containing credentials for authenticating with Google Cloud services, particularly Google BigQuery.
- `dev_trial.json`  : JSON file containing credentials for authenticating with Vertex AI.

The JSON file can be accessed [here](https://drive.google.com/drive/folders/11lTvchvHQaGi2Xhk2usUF_MjpVPRrHfm?usp=drive_link).
