from http.client import HTTPException

from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str
class MonthlyExpense(BaseModel):
    month:str
    total_expense:float


class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expense_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database")

    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expenses updated Successfully."}


@app.post("/Analytics/")
def get_analytics(date_range: DateRange):
    # print("Received:", date_range.start_date, type(date_range.start_date))

    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch expenses summary from the database")
    total = sum([row["total"] for row in data])
    breakdown = {}
    for row in data:
        percentage = (row["total"] / total) * 100 if total != 0 else 0
        breakdown[row["category"]] = {
            "total": row["total"],
            "percentage": percentage
        }
    return breakdown


@app.post("/monthly_wise_expenses/", response_model=List[MonthlyExpense])
def get_monthly_wise_expense():
    data = db_helper.fetch_expense_monthly()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch expenses summary from the database")
    else:
        return data
