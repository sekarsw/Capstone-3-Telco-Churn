import streamlit as st

home_page = st.Page(
    page = 'pages/home.py',
    title = 'Home',
    default = True,
    icon = ':material/home:'
)

model_page = st.Page(
    page = 'pages/model_performance.py',
    title = 'Model Performance',
    icon = ':material/analytics:'
)

predict_page = st.Page(
    page = 'pages/predict.py',
    title = 'Predict Customer Churn',
    icon = ':material/smart_toy:'
)

nav = st.navigation(pages = [home_page, model_page, predict_page])

nav.run()