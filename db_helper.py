import mysql.connector
from contextlib import contextmanager

from logging_setup import setup_logger

logger = setup_logger("db_helper")


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="johan@4545",
        database="expense_manager",
    )

    if connection.is_connected():
        print("connection successful.")
    else:
        print("Failed in connecting to a database.")
    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    connection.close()
    cursor.close()


def fetch_all_records():
    logger.info("This function fetch all the records from databases.")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("SELECT * from expenses")
        expenses = cursor.fetchall()

        for expense in expenses:
            print(expense)


def fetch_expense_for_date(expense_date):
    logger.info("This function is amazing.")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


        


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"This function:{insert_expense} takes as an argument expense_date:{expense_date}, amount:{amount}"
                f"category:{category}, notes:{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses(expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
                       (expense_date, amount, category, notes))


def delete_expense_for_date(expense_date):
    logger.info("This function is going well!!!")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start:{start_date} end:{end_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            """
            SELECT category, SUM(amount) as total
            FROM expenses WHERE expense_date BETWEEN %s and %s 
            GROUP BY category;""", (start_date, end_date)
        )
        data = cursor.fetchall()
        return data


def fetch_expense_monthly():
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(

            """
        SELECT DATE_FORMAT(expense_date, '%Y-%m') AS month,
        SUM(amount) AS total_expense
        FROM expenses
        GROUP BY month
        ORDER BY month DESC;"""

        )
        data = cursor.fetchall()
        return data




if __name__ == "__main__":
    

    
    



