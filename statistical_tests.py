import streamlit as st
import numpy as np
from scipy import stats
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.proportion import proportions_ztest

def run_stat_tests(df):
    st.subheader("Statistical Tests")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    test = st.selectbox("Choose test", ["Z-test", "T-test", "Proportion Z-test"])
    col = st.selectbox("Select column for test", numeric_cols)

    if test == "Z-test":
        z_score, p_val = ztest(df[col])
        st.write(f"Z = {z_score:.3f}, P = {p_val:.3f}")

    elif test == "T-test":
        t_stat, p_val = stats.ttest_1samp(df[col].dropna(), popmean=0)
        st.write(f"T = {t_stat:.3f}, P = {p_val:.3f}")

    elif test == "Proportion Z-test":
        threshold = st.slider("Threshold value", float(df[col].min()), float(df[col].max()), float(df[col].mean()))
        successes = np.sum(df[col] > threshold)
        trials = len(df[col])
        stat, p_val = proportions_ztest(successes, trials, 0.5)
        st.write(f"Z = {stat:.3f}, P = {p_val:.3f}")