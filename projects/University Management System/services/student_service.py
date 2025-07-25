import sys
import os
import json
from datetime import datetime

now = datetime.now()
year = now.year
enrollment_date = now.strftime("%Y-%m-%d")
UNIVERSITY_NAME = "Addis Ababa University"
print(f"Current Year: {year}, Enrollment Date: {enrollment_date}")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from utils.id_generator import id_generator
from utils.file_handler import load_data, append_data, save_data
STUDENT_FILE = os.path.join(BASE_DIR, '..', 'data', 'student_data.json')
students = load_data(STUDENT_FILE)

program_level = ""
print("Choose student's Program Level :")
program_levels = ['Undergraduate', 'Postgraduate']
for i, level in enumerate(program_levels, start=1):
    print(f"{i}. {level}")
choice = int(input("Enter your choice (1 or 2): "))

if choice in [1, 2]:
    selected_level = program_levels[choice - 1]
    program_level = selected_level
else:
    print("Invalid choice.")

#print(students)
Student_department = ""
undergrad_departments = ['Computer Science', 'Information Technology', 'Software Engineering', 'Data Science']
postgrad_departments = ['Data Analytics', 'Cyber Security', 'Cloud Computing', 'AI and Machine Learning']

if program_level == 'Undergraduate':
    departments = undergrad_departments
elif program_level == 'Postgraduate':
    departments = postgrad_departments

print("Choose Student Department: ")
for i in range(len(departments)):
    print(f"{i + 1}. {departments[i]}")

choice = int(input("Enter your choice (1-4): "))

if choice in range(1, 5):
    selected_department = departments[choice - 1]
    Student_department = selected_department
else:
    print("Invalid choice.")   

print(Student_department)

def add_new_student():
    students = load_data(STUDENT_FILE)
    full_name = input("Enter student's full name: ").strip()
    gender = input("Enter student's gender (M/F): ").strip().upper()
    age = int(input("Enter student's age: ").strip())
    department = input("Enter student's department: ").strip()
    year_of_study = int(input("Enter student's year of study: ").strip())
    status = input("Enter student's status (Active/Inactive): ").strip().capitalize()
    #program_level = input("Enter student's type (Undergraduate/Postgraduate): ").strip().capitalize()
    semester = input("Enter student's semester (I/II): ").strip()
    student_id = id_generator("STUD", year)
    new_student = {
        'student_id': student_id,
        'program_level': program_level,
        'name': full_name,
        'gender': gender,
        'age': age,
        'enrollment_date': enrollment_date,
        'university': UNIVERSITY_NAME,
        'department': department,
        "year_of_study": year_of_study,
        "status": status,
        'year': year,
        'student_id': student_id,
        "student_type": "Regular",
        "semester": semester,
        "courses": [],
        "gpa": 0.0,
    }
    students.append(new_student)
    save_data(STUDENT_FILE, students)
    print(f"Student {full_name} has been successfully registered with ID {student_id}")

def show_all_students():
    students = load_data(STUDENT_FILE)
    if not students:
        print("No students found.")
        return
    # Print table header
    print(f"{'ID':<12} {'Name':<25} {'Department':<20} {'Year':<6} {'Status':<10} {'Program':<15} {'Semester':<8}")
    print("-" * 100)
    # Print each student in a row
    for student in students:
        print(f"{student['student_id']:<12} {student['name']:<25} {student['department']:<20} {student['year_of_study']:<6} {student['status']:<10} {student['program_level']:<15} {student['semester']:<8}")
