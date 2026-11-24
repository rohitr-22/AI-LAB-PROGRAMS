# Student Marks, Percentage and Grade
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))
total = 0

# Loop to collect marks for each subject
for i in range(1, n + 1):
    mark = float(input(f"Enter mark for Subject {i}: "))
    total += mark

# Calculate percentage
percentage = total / n

# Determine grade and performance status using conditional statements
if percentage >= 90:
    grade = "A+"
    performance = "Outstanding"
elif percentage >= 80:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage >= 60:
    grade = "C"
    performance = "Good"
elif percentage >= 50:
    grade = "D"
    performance = "Average"
else:
    grade = "F"
    performance = "Needs Improvement"

# Display the final academic performance report
print("\n--- Academic Performance ---")
print("Student Name :", name)
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Performance  :", performance)
