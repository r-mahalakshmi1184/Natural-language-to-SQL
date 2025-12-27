import pandas as pd
import sqlite3

# Load your CSV file
df = pd.read_csv("employee_salary.csv")  # make sure this matches your CSV name

# Connect to SQLite database (will create file if it doesn't exist)
conn = sqlite3.connect("employee_salary.db")
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    EmployeeID INTEGER,
    Name TEXT,
    Department TEXT,
    Position TEXT,
    Salary INTEGER
)
""")

# Insert data into table
df.to_sql("employees", conn, if_exists="replace", index=False)

print("employee_salary.csv loaded into 'employees' table in employee_salary.db")

conn.commit()
conn.close()
