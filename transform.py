import pandas as pd

import pandas as pd

def transform_data(employees, departments):

    employees = employees.dropna(subset=["salary"])

    employees["salary"] = employees["salary"].astype(int)

    employees["bonus"] = employees["salary"] * 0.10

    merged = pd.merge(
        employees,
        departments,
        on="department_id",
        how="inner"
    )

    summary = (
        merged
        .groupby("department_name")
        .agg(
            average_salary=("salary", "mean"),
            total_salary=("salary", "sum"),
            employee_count=("salary", "count")
        )
        .reset_index()
    )

    return merged, summary




# Two employees don't have salaries.
# Should we remove them?

# There are three possibilities.

# employees = employees.dropna(subset=["salary"]) #Delete them
# employees["salary"] = employees["salary"].fillna(0) #Replace them
# employees["salary"] = employees["salary"].fillna(
#     employees["salary"].mean()
# )   #Average of Salary