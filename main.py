from extract import extract_data
from transform import transform_data
from load import load_data
from extract import extract_data

def main():

    employees, departments = extract_data()

    merged, summary = transform_data(
        employees,
        departments
    )

    load_data(
        merged,
        summary
    )

    print("ETL Completed Successfully!")

if __name__ == "__main__":
    main()


# These are the main methoda to explore the data once extraction is over 
#Next step will we should do is validation, checck the data types, null values, duplicates, etc.

# employees.head()

# employees.tail()

# employees.shape

# employees.columns

# employees.dtypes

# employees.info()

# employees.describe()

# employees.isnull()

# employees.isnull().sum()


# employees = employees.dropna(subset=["salary"])
# employees["salary"] = employees["salary"].astype(int)
# print(employees.dtypes)


# Show employees earning above 60,000.

# employees["bonus"] = employees["salary"] * 0.10

# high_salary = employees[
#     employees["salary"] > 60000
# ]

# IT employees earning above 50k.
# employees[
#     (employees["department_id"] == 101)
#     &
#     (employees["salary"] > 50000)
# ]


# Highest salary first.

# employees = employees.sort_values(
#     by="salary",
#     ascending=False
# )


