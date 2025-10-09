import streamlit as st
from pandas import read_csv

st.set_page_config(page_title="Modify Dataset", page_icon="✂️", layout="wide")

st.title("✂️ Modify Dataset")
st.markdown(
    """
    This page lets you interactively **clean and transform your dataset** before analysis.  
    """
)

st.write("---")

st.subheader("🧾 Column Operations")

if 'df' not in st.session_state:
    st.session_state['df'] = read_csv('datasets/steam_sales.csv')

drop_cols = st.multiselect("Select columns to drop", st.session_state['df'].columns)
if st.button("Confirm Drop Columns"):
    if drop_cols:
        if len(drop_cols) == 11:
            st.warning("⚠️ At least 1 column is required.")
        else:
            st.session_state['df'] = st.session_state['df'].drop(columns=drop_cols)
            st.info(f"🗑️ Dropped columns: {drop_cols}")
    else:
        st.warning("⚠️ No columns selected to drop.")

st.write("✏️ Rename Columns")
col_to_rename = st.selectbox("Select column to rename", st.session_state['df'].columns)
new_col_name = st.text_input("Enter new column name")
if st.button("Confirm Rename"):
    if new_col_name.strip():
        st.session_state['df'] = st.session_state['df'].rename(columns={col_to_rename: new_col_name})
        st.success(f"Renamed `{col_to_rename}` → `{new_col_name}`")
    else:
        st.warning("⚠️ Please enter a valid new column name.")

st.write("---")

st.subheader("⚠️ Handle Missing Values")
missing_option = st.radio("Choose an action", ["Do Nothing", "Drop Rows with Missing Values", "Fill Missing Values"])
if missing_option == "Drop Rows with Missing Values":
    if st.button("Confirm Drop Missing Rows"):
        st.session_state['df'] = st.session_state['df'].dropna()
        st.info("🗑️ Dropped rows containing missing values.")
elif missing_option == "Fill Missing Values":
    fill_value = st.text_input("Enter a value to fill missing cells with")
    if st.button("Confirm Fill Missing Values"):
        if fill_value:
            st.session_state['df'] = st.session_state['df'].fillna(fill_value)
            st.info(f"✅ Filled missing values with `{fill_value}`")
        else:
            st.warning("⚠️ Please provide a value to fill missing cells.")

st.write("---")

st.subheader("🔍 Filter Rows")
filter_col = st.selectbox("Select column to filter", st.session_state['df'].columns)
unique_vals = st.session_state['df'][filter_col].unique().tolist()
selected_vals = st.multiselect("Choose values to keep", unique_vals)
if st.button("Confirm Filter Rows"):
    if selected_vals:
        st.session_state['df'] = st.session_state['df'][st.session_state['df'][filter_col].isin(selected_vals)]
        st.info(f"✅ Filtered rows where `{filter_col}` is in {selected_vals}")
    else:
        st.warning("⚠️ Please select values to filter.")

st.write("---")

# Reset index
if st.checkbox("♻️ Reset index after modifications"):
    if st.button("Confirm Reset Index"):
        st.session_state['df'] = st.session_state['df'].reset_index(drop=True)
        st.success("✅ Index reset successfully!")

# Final dataset preview
st.subheader("📊 Modified Dataset Preview")
st.dataframe(st.session_state['df'].head())

# Download option
st.download_button(
    label="💾 Download Modified Dataset (CSV)",
    data=st.session_state['df'].to_csv(index=False).encode("utf-8"),
    file_name="modified_dataset.csv",
    mime="text/csv",
)

def set_data():
    st.session_state['df'] = read_csv('datasets/steam_sales.csv')

st.button(
    label="🔄️ Reload Data",
    on_click=set_data,
)

