import pandas as pd

n = int(input("Enter number of students: "))

names = []
departments = []
attendance = []
marks = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    names.append(input("Enter Name: "))
    departments.append(input("Enter Department: "))
    
    a = input("Enter Attendance (or blank): ")
    attendance.append(float(a) if a else None)

    m = input("Enter Mark (or blank): ")
    marks.append(float(m) if m else None)

data = {
    "Name": names,
    "Department": departments,
    "Attendance": attendance,
    "Mark": marks
}

df = pd.DataFrame(data)

print("\n--- Original Dataset ---")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Missing value treatment
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())


# Remove duplicate records
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))
