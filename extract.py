import pandas as pd
from database import engine

def extract_data():
    employees = pd.read_sql(
        """
        SELECT *
        FROM employees
        """,
        engine
    )

    departments = pd.read_sql(
        """
        SELECT *
        FROM departments
        """,
        engine
    )

    return employees, departments