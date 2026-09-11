"""Streamlit component and layout exercises from Lesson 11."""
import streamlit as st

st.title("My First Streamlit App")
st.header("Section 1")
st.subheader("Header")
st.subheader("Subheader")
st.text("Simple text")
st.markdown("**Bold** and *italic* text")
st.write("Automatic data display")
st.code("print('Hello World')", language="python")
st.latex(r"\int_{a}^{b} x^2 dx")

st.header("Section 2")
name = st.text_input("Enter your name", "Amara Diallo")
description = st.text_area("Description", "Write something...")
age = st.number_input("Age", min_value=0, max_value=120, value=25)
score = st.slider("Score", 0, 100, 50)
option = st.selectbox("Choose an option", ["A", "B", "C"])
options = st.multiselect("Multiple options", ["X", "Y", "Z"])
date = st.date_input("Select date")
time = st.time_input("Select time")
if st.button("Click me"):
    st.write("Button clicked!")
if st.checkbox("Show/Hide"):
    st.write("Visible content")

st.header("Section 3")
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")
with st.expander("Click to expand"):
    st.write("Expanded content here")
st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"])
