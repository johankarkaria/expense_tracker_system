from backend import db_helper


def test_fetch_expense_for_date():
    expense = db_helper.fetch_expense_for_date("2024-08-15")

    assert len(expense) == 1
    assert expense[0]["amount"] == 10.0
    assert expense[0]["category"] == "Shopping"
    assert expense[0]["notes"] == "Bought potatoes"
