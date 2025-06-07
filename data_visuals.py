import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def show_visualizations(df):
    st.subheader("Visualizations")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numeric_cols:
        st.warning("No numeric data available for plotting.")
        return

    selected_cols = st.multiselect("Select columns for visualization", numeric_cols, default=numeric_cols)

    if len(selected_cols) >= 1:
        corr = df[selected_cols].corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        col = st.selectbox("Select column for histogram", selected_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

        if len(selected_cols) >= 2:
            x = st.selectbox("X axis", selected_cols)
            y = st.selectbox("Y axis", selected_cols, index=1)
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[x], y=df[y], ax=ax)
            st.pyplot(fig)