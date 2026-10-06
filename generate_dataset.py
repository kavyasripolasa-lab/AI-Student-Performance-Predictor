import pandas as pd
import random

random.seed(42)

names = [
    "Kavya", "Rahul", "Anjali", "Arjun", "Priya",
    "Sai", "Sneha", "Rohit", "Aarav", "Neha",
    "Varun", "Keerthi", "Manoj", "Divya", "Vikram",
    "Pooja", "Harsha", "Sanjana", "Kiran", "Nithin"
]

students = []

for i in range(1, 201):

    name = random.choice(names) + f" {i}"
    roll_number = f"AI{2026}{i:03d}"

    attendance = random.randint(55, 100)
    study_hours = round(random.uniform(1, 7), 1)
    assignment_score = random.randint(45, 100)
    mid_marks = random.randint(40, 100)
    previous_gpa = round(random.uniform(5.5, 9.8), 1)

    final_score = (
        attendance * 0.20
        + study_hours * 4
        + assignment_score * 0.20
        + mid_marks * 0.35
        + previous_gpa * 2
        + random.uniform(-5, 5)
    )

    final_score = round(max(35, min(100, final_score)), 1)

    students.append([
        name,
        roll_number,
        attendance,
        study_hours,
        assignment_score,
        mid_marks,
        previous_gpa,
        final_score
    ])

data = pd.DataFrame(
    students,
    columns=[
        "Student_Name",
        "Roll_Number",
        "Attendance",
        "Study_Hours",
        "Assignment_Score",
        "Mid_Marks",
        "Previous_GPA",
        "Final_Score"
    ]
)

data.to_csv("student_data.csv", index=False)

print("Student dataset created successfully!")
print("Total students:", len(data))