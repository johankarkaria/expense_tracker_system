import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"


def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        pay_load = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/Analytics/", json=pay_load)
        data = response.json()
        structured_data = {
            "category": list(data.keys()),
            "total": [data[category]["total"] for category in data],
            "Percentage": [data[category]["percentage"] for category in data]

        }
        df = pd.DataFrame(structured_data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)
        st.title("Expense Breakdown by Category")
        st.bar_chart(data=df_sorted.set_index("category")["Percentage"], width=0, height=0, use_container_width=True)
        df_sorted["total"] = df_sorted["total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
        st.table(df_sorted)
