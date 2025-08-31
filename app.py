import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from monthly_expense_ui import get_monthly_expenses

st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics", "Monthly_expenses"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    get_monthly_expenses()
