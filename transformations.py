import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def transform_data(df):
    st.subheader("Data Transformations")

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numeric_cols:
        return df

    option = st.selectbox("Select a transformation", ["None", "Standardize", "Normalize", "Log Transform"])
    col = st.selectbox("Select column for transformation", numeric_cols)

    try:
        if option == "Standardize":
            df[col] = StandardScaler().fit_transform(df[[col]])
        elif option == "Normalize":
            df[col] = MinMaxScaler().fit_transform(df[[col]])
        elif option == "Log Transform":
            df[col] = np.log1p(df[col])
        if option != "None":
            st.success(f"{option} applied to {col}")
    except Exception as e:
        st.error(f"Error transforming data: {e}")

    return df