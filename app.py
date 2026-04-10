import streamlit as st
from expense_manager import add_expense, view_expenses, total_expense
from storage import load_expenses, save_expenses

st.title("Expense Tracker")

expenses = load_expenses()

menu = st.sidebar.selectbox("Menu", ["Add Expense", "View Expenses", "Total"])

if menu == "Add Expense":
    st.subheader("Add Expense")
    amount = st.number_input("Amount", min_value=0.0)
    category = st.text_input("Category")

    if st.button("Add"):
        add_expense(expenses, amount, category)
        save_expenses(expenses)
        st.success("Expense added!")

elif menu == "View Expenses":
    st.subheader("All Expenses")
    if expenses:
        st.write(expenses)
    else:
        st.info("No expenses yet")

elif menu == "Total":
    st.subheader("Total Expense")
    total = total_expense(expenses)
    st.write(f"Total: {total}")