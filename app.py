import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.data_summary import show_data_summary
from utils.data_cleaning import clean_data
from utils.data_visuals import show_visualizations
from utils.transformations import transform_data
from utils.statistical_tests import run_stat_tests

st.set_page_config(page_title="Statistical Analysis App", layout="wide")
st.title("Simple Statistical Analysis App")
st.markdown("Upload your dataset and get quick statistical insights and visualizations")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("Preview of uploaded Data")
    st.dataframe(df.head())

    show_data_summary(df)
    df = clean_data(df)
    df = transform_data(df)
    show_visualizations(df)
    run_stat_tests(df)