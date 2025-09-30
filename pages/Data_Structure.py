import streamlit as st
from pandas import read_csv, DataFrame

st.set_page_config(page_title="Explore Data Structure", page_icon="🔎", layout="wide")

st.title("🔎 Explore Data Structure")
st.markdown(
    """
    This page gives you a quick overview of the dataset, including its 
    **size, features, data types, missing values**, and a basic summary.  
    """
)

if 'df' not in st.session_state:
    st.session_state['df'] = read_csv('datasets/steam_sales.csv')

st.subheader("👀 Dataset Preview")
st.dataframe(st.session_state['df'].head())

st.subheader("📏 Dataset Shape")
st.write(f"- **Rows:** {st.session_state['df'].shape[0]}")
st.write(f"- **Columns:** {st.session_state['df'].shape[1]}")

st.subheader("🧾 Features & Data Types")
col_info = DataFrame({
    "Column": st.session_state['df'].columns,
    "Data Type": st.session_state['df'].dtypes.astype(str),
    "Missing Values": st.session_state['df'].isnull().sum(),
    "Unique Values": st.session_state['df'].nunique()
})
st.dataframe(col_info)

st.subheader("📊 Basic Statistics (Numeric Columns)")
st.dataframe(st.session_state['df'].describe().T)

