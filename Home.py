import streamlit as st

# Page config
st.set_page_config(
    page_title="Steam Sales Data Visualization",
    page_icon="🎮",
    layout="wide"
)

# Main Title
st.title("🎮 Steam Sales Data Visualization Project")
st.markdown("### Unlock insights into Steam’s sales trends with data-driven visualizations")

st.write("---")  # Divider

# Objective Section
st.header("📌 Project Objective")
st.markdown(
    """
    This project explores **time-series data of Steam Sales** to uncover hidden patterns 
    and provide insights for both **gamers** and **developers**.
    """
)

st.write("---")

# Audience Section with Columns
st.subheader("👥 Who Can Benefit?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎮 For Gamers")
    st.markdown(
        """
        - ⏳ Find out **when to expect the best discounts** on games  
        - 📅 Discover **which time of year** most games go on sale  
        - 🛒 Plan purchases around major sale events  
        """
    )

with col2:
    st.markdown("### 🛠️ For Developers")
    st.markdown(
        """
        - 💬 Analyze how **discounts affect reviews and player sentiment**  
        - 📈 Identify **market trends** around seasonal sales  
        - 🎯 Understand how pricing strategies impact engagement  
        """
    )

st.write("---")

# Project Pages Section
st.subheader("📑 Project Pages")
st.markdown(
    """
    The project consists of three main interactive pages:  

    1. **🔎 Explore Data Structure** – View dataset shape, features, missing values, and data types.
    2. **⚙️ Data Operations** - Perform operations on the dataset to customize results.
    3. **❓ Common Questions** – Get quick answers to key questions (e.g., when are most discounts offered?).  
    4. **📈 Custom Visualizations** – Create your own plots by choosing features and chart types.  
    """
)

st.write("---")

# Closing / Call to Action
st.subheader("🚀 What’s Next?")
st.markdown(
    """
    Navigate through the project using the sidebar to explore the data, 
    answer key questions, and generate your own visualizations!  
    """
)
