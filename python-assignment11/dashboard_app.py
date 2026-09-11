"""A small product dashboard for the Lesson 11 Streamlit exercise."""
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

np.random.seed(42)
df = pd.DataFrame({
    "Product": ["Product A", "Product B", "Product C", "Product D"],
    "Sales": np.random.randint(100, 500, size=4),
    "Profit": np.random.randint(20, 100, size=4),
})
st.sidebar.header("Filter Options")
selected_product = st.sidebar.selectbox("Select Product", df["Product"])
filtered_df = df[df["Product"] == selected_product]
st.title("Simple Product Dashboard")
col1, col2 = st.columns(2)
with col1:
    st.metric("Sales", f"${filtered_df['Sales'].iloc[0]:,}")
with col2:
    st.metric("Profit", f"${filtered_df['Profit'].iloc[0]:,}")
st.subheader("Sales and Profit Comparison")
st.plotly_chart(px.bar(df, x="Product", y=["Sales", "Profit"], barmode="group"), width="stretch")
