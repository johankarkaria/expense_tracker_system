import streamlit as st
import requests
import pandas as pd


API_URL = "http://127.0.0.1:8000"


def get_monthly_expenses():
    if st.button("Monthly_expenses"):
        response = requests.post(f"{API_URL}/monthly_wise_expenses/")
        data = response.json()
        # st.json(data)

        structured_data = {
            "month": [expense["month"] for expense in data],
            "total": [expense["total_expense"] for expense in data]
        }

        df = pd.DataFrame(structured_data)
        df["month_dt"] = pd.to_datetime(df["month"], format="%Y-%m")
        df["month_number"] = df["month_dt"].dt.month
        df["month_name"] = df["month_dt"].dt.strftime("%B")
        total_sum = df["total"].sum()
        df["percentage"] = (df["total"] / total_sum) * 100

        df = df.sort_values("month_number")
        df = df.set_index("month_number")

        df_chart = df.set_index("month_name")[["percentage"]]
        st.title("Expense Breakdown by Months")
        st.bar_chart(data=df_chart, width=0, height=0, use_container_width=True)

        df["total"] = df["total"].map("{:.2f}".format)
        df["percentage"] = df["percentage"].map("{:.2f}%".format)

        df = df[["month_name", "total", "percentage"]]

        st.table(df)
