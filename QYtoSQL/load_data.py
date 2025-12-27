import pandas as pd
import random

# Sample data
departments = ["HR", "Finance", "Engineering", "Sales", "Marketing"]
positions = ["Manager", "Senior", "Junior", "Intern", "Lead"]

# Generate 50 rows
data = []
for i in range(1, 51):
    employee = {
        "EmployeeID": i,
        "Name": f"Employee{i}",
        "Department": random.choice(departments),
        "Position": random.choice(positions),
        "Salary": random.randint(30000, 120000)
    }
    data.append(employee)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("employee_salary.csv", index=False)
print("employee_salary.csv created with 50 rows")
