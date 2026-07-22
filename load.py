from database import engine

def load_data(merged, summary):

    merged.to_sql(
        name="processed_employees",
        con=engine,
        if_exists="replace",
        index=False
    )

    summary.to_sql(
        name="employee_summary",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data Loaded Successfully!")