import pandas as pd

n = int(input("Enter number of students: "))

names = []
rollno = []
departments = []
marks_list = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    rollno.append(int(input("Enter Roll Number: ")))
    names.append(input("Enter Name: "))
    departments.append(input("Enter Department: "))
    marks_list.append(int(input("Enter Mark: ")))

# Pandas Series
marks = pd.Series(marks_list)

print("\n--- Pandas Series ---")
print(marks)

# DataFrame
data = {
    "RollNo": rollno,
    "Name": names,
    "Department": departments,
    "Mark": marks_list
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

print("\nAverage Mark:", round(df["Mark"].mean(), 2))

print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])
