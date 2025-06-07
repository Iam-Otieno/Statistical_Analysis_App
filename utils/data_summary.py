import streamlit as st
import pandas as pd
import numpy as np
import io

def show_data_summary(df):
    st.subheader("📊 Descriptive Statistics")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if numeric_cols:
        selected_cols = st.multiselect("Select columns", numeric_cols, default=numeric_cols)
        if selected_cols:
            stats = df[selected_cols].describe().T
            stats["mode"] = df[selected_cols].mode().iloc[0]
            st.dataframe(stats)
    else:
        st.info("No numeric columns to describe.")

    st.subheader("📄 DataFrame Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    st.subheader("❓ Missing Values")
    st.dataframe(df.isnull().sum().to_frame(name="Missing Values"))

    st.subheader("🔢 Unique Values per Column")
    unique_vals = pd.DataFrame({col: df[col].nunique() for col in df.columns}, index=["Unique Values"]).T
    st.dataframe(unique_vals)

    st.subheader("📑 Data Types")
    st.dataframe(df.dtypes.astype(str).to_frame(name="Data Type"))

    st.subheader("📐 Shape of the DataFrame")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    st.subheader("📈 Correlation Matrix")
    if len(numeric_cols) >= 2:
        st.dataframe(df[numeric_cols].corr())
    else:
        st.info("Not enough numeric columns to compute correlation.")
