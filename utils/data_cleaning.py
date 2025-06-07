import streamlit as st
import pandas as pd
import numpy as np

def clean_data(df):
    st.subheader("Data Cleaning")

    df.drop_duplicates(inplace=True)
    st.success("Duplicate rows removed.")

    if df.isnull().values.any():
        method = st.selectbox("Fill missing values with", ["Mean", "Median", "Mode", "Drop"])
        if method == "Mean":
            df.fillna(df.mean(numeric_only=True), inplace=True)
        elif method == "Median":
            df.fillna(df.median(numeric_only=True), inplace=True)
        elif method == "Mode":
            for col in df.columns:
                df[col].fillna(df[col].mode()[0], inplace=True)
        elif method == "Drop":
            df.dropna(inplace=True)
        st.success(f"Missing values handled using {method}")
    else:
        st.info("No missing values to handle.")

    col = st.selectbox("Select column to change data type", df.columns)
    dtype = st.selectbox("Select new data type", ["int", "float", "str", "category"])
    try:
        df[col] = df[col].astype(dtype)
        st.success(f"Converted {col} to {dtype}")
    except Exception as e:
        st.error(f"Failed to convert {col}: {e}")

    return df