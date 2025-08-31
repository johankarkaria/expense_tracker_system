import streamlit as st
from datetime import datetime

import requests

API_URL = "http://127.0.0.1:8000"

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])


def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1))
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("failed to retrieve expenses.")
        existing_expenses = []
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("amount")
        with col2:
            st.subheader("category")
        with col3:
            st.subheader("notes")
        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            with col1:
                amount_input = st.number_input(label="amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="category", options=categories, key=f"category_{i}",
                                              index=categories.index(category),
                                              label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")
            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense["amount"] > 0]
            requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated successfully")
            else:
                st.error("Failed to update Expenses")
