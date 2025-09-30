import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Steam Sales Insights", layout="wide")
st.title("🎮 Steam Sales Data Dashboard")

# Load dataframe from session_state
df = st.session_state['df']

# Sidebar filters
st.sidebar.header("Filters")
min_reviews, max_reviews = st.sidebar.slider(
    "Filter by number of reviews:",
    int(df['#Reviews'].min()),
    int(df['#Reviews'].max()),
    (int(df['#Reviews'].min()), int(df['#Reviews'].max()))
)
filtered_df = df[(df['#Reviews'] >= min_reviews) & (df['#Reviews'] <= max_reviews)]

# --- Graph 1: Distribution of Discounts ---
st.subheader("Discount Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['Discount%'], bins=30, kde=True, ax=ax, color="skyblue")
ax.set_xlabel("Discount %")
ax.set_ylabel("Count")
st.pyplot(fig)

# --- Graph 2: Top 10 Games by Number of Reviews ---
st.subheader("Top 10 Games by Reviews")
top_reviews = filtered_df.sort_values(by="#Reviews", ascending=False).head(10)
fig, ax = plt.subplots()
sns.barplot(y="Game Name", x="#Reviews", data=top_reviews, ax=ax, palette="viridis")
ax.set_xlabel("Number of Reviews")
ax.set_ylabel("")
ax.set_title("Top 10 Most Reviewed Games")
st.pyplot(fig)

# --- Graph 3: Price vs Rating ---
st.subheader("Price vs Rating")
fig, ax = plt.subplots()
sns.scatterplot(x="Price (€)", y="Rating", data=filtered_df, alpha=0.6, ax=ax)
ax.set_xlabel("Price (€)")
ax.set_ylabel("Rating")
st.pyplot(fig)

# --- Graph 4: Platform Availability ---
st.subheader("Platform Availability")
platform_counts = {
    "Windows": filtered_df['Windows'].sum(),
    "Linux": filtered_df['Linux'].sum(),
    "MacOS": filtered_df['MacOS'].sum()
}
fig, ax = plt.subplots()
ax.pie(platform_counts.values(), labels=platform_counts.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title("Games Available per Platform")
st.pyplot(fig)

# --- Graph 5: Average Discount by Release Year ---
st.subheader("Average Discount by Release Year")
df['Year'] = pd.to_datetime(df['Release Date'], errors='coerce').dt.year
avg_discount = filtered_df.groupby('Year')['Discount%'].mean().dropna()
fig, ax = plt.subplots()
avg_discount.plot(kind='bar', ax=ax, color='coral')
ax.set_ylabel("Average Discount %")
ax.set_xlabel("Release Year")
ax.set_title("Average Discount per Release Year")
st.pyplot(fig)

st.success("✅ Dashboard loaded successfully!")
