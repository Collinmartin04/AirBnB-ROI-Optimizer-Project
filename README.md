# 🏡 Airbnb ROI Optimizer – Nashville

This project is a Streamlit dashboard that helps Airbnb hosts and investors **maximize revenue and choose the most profitable neighborhoods** in Nashville, TN. It uses real listing data from Inside Airbnb and provides an interactive tool to simulate earnings based on pricing strategy, room type, and availability.

---

## 🚀 Features

- 💰 **Top 10 most profitable neighborhoods** by average monthly revenue
- 🛏️ **Revenue comparison by room type**
- 📊 **Interactive ROI calculator** based on nightly price, availability, and occupancy rate
- 📍 Full summary of revenue and listings across Nashville neighborhoods
- ✅ Clean, intuitive design — ready to deploy with Streamlit Cloud

---

## 📂 Project Structure

AirBnB-ROI-Optimizer/
├── data/
│ └── processed/
│ └── nashville_cleaned.csv # Cleaned listing data
├── src/
│ └── clean_listings.py # Preprocessing logic
├── dashboard/
│ └── app.py # Streamlit dashboard app
├── notebooks/
│ └── analysis.ipynb # Optional: EDA and exploration
├── README.md # You are here
├── requirements.txt # Python packages
└── .gitignore

---

## 📈 Sample Insights

> 🥇 **District 34** has the highest estimated average monthly revenue: **$5,909.27**
>
> 🛏️ Entire homes average significantly higher revenue than shared or private rooms
>
> 📉 Undervalued neighborhoods were found with potential ROI gains over **20%**

---

## 📦 Tech Stack

- Python 3
- Pandas
- Streamlit
- Matplotlib / Seaborn
- [Inside Airbnb Open Data](http://insideairbnb.com/)

---

## 🧪 Getting Started Locally

### ✅ Step 1: Install dependencies

pip install -r requirements.txt

### ✅ Step 2: Run the app

cd dashboard
streamlit run app.py

---

## 📬 Contact
Created by: Collin Martin
LinkedIn: https://www.linkedin.com/in/collin-martin-6461482b5/
GitHub: https://github.com/Collinmartin04
