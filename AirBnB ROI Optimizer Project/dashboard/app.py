import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("../data/processed/nashville_cleaned.csv")

st.set_page_config(page_title="Airbnb ROI Dashboard", layout="wide")
st.title("🏡 Nashville Airbnb ROI Dashboard")
st.markdown("Gain insights on Nashville Airbnb pricing, profitability, and rental strategy.")

# ===== Sidebar Revenue Calculator =====
st.sidebar.header("📊 Estimate Your Monthly Revenue")
room_type = st.sidebar.selectbox("Room Type", df["room_type"].unique())
price = st.sidebar.slider("Nightly Price ($)", min_value=30, max_value=1000, value=150)
availability = st.sidebar.slider("Availability (days per year)", 30, 365, 180)
occupancy_rate = st.sidebar.slider("Occupancy Rate (0–1)", 0.1, 1.0, 0.6)

monthly_availability = availability / 12
estimated_revenue = price * monthly_availability * occupancy_rate

st.sidebar.markdown(f"### 💵 Est. Monthly Revenue: **${estimated_revenue:,.2f}**")

# ===== Section 1: Top Neighborhoods =====
st.subheader("💰 Top 10 Profitable Neighborhoods (Avg. Revenue)")

top_neighborhoods = df.groupby("neighbourhood")["estimated_monthly_revenue"] \
                      .mean().sort_values(ascending=False).head(10).round(2)

top_neighborhoods = top_neighborhoods.apply(lambda x: f"${x:,.2f}")

st.dataframe(top_neighborhoods.reset_index().rename(columns={
    "neighbourhood": "Neighborhood",
    "estimated_monthly_revenue": "Avg. Monthly Revenue ($)"
}))

# ===== Section 2: Revenue by Room Type =====

st.subheader("🏘️ Average Revenue by Room Type")

room_type_rev = df.groupby("room_type")["estimated_monthly_revenue"] \
                  .mean().sort_values(ascending=False).round(2)

room_type_rev = room_type_rev.apply(lambda x: f"${x:,.2f}")

st.table(room_type_rev.reset_index().rename(columns={
    "room_type": "Room Type",
    "estimated_monthly_revenue": "Avg. Revenue ($)"
}))


# ===== Section 3: Full Revenue Table =====

st.subheader("📍 Full Revenue Table by Neighborhood")
summary = df.groupby("neighbourhood").agg(
    listings=('id', 'count'),
    avg_price=('price', 'mean'),
    avg_revenue=('estimated_monthly_revenue', 'mean')
).sort_values(by='avg_revenue', ascending=False).round(2)

# Format price and revenue as strings with $ signs
summary["avg_price"] = summary["avg_price"].apply(lambda x: f"${x:,.2f}")
summary["avg_revenue"] = summary["avg_revenue"].apply(lambda x: f"${x:,.2f}")

st.dataframe(summary.reset_index().rename(columns={
    "neighbourhood": "Neighborhood",
    "listings": "Listings",
    "avg_price": "Avg. Price",
    "avg_revenue": "Avg. Monthly Revenue"
}))
