import json
import os

#load data of the txt file
def load_data(filename='student_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                print("Warning: File is corrupted. Starting fresh.")
                return {}
    else:
        return {}

#save data in to the file
def save_data(data, filename='student_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

#Generates ID
def id_generator(students, start = 1000):
    if not students:
        return str(start)
    existing_ids = [int(sid) for sid in students.keys()]
    new_id = max(existing_ids) + 1
    return str(new_id)

#average calculator
def calculate_average(scores):
    total = 0.0
    length = len(scores)
    for avg in scores.values():
        total += avg
    return total / length

#changes student score to grade
def score_to_grade(student_score):

    if 80 <= student_score <= 100:
        grade = 'A'
    elif 70 <= student_score <= 79:
        grade = 'B'
    elif 60 <= student_score <= 69:
        grade = 'C'
    elif 50 <= student_score <= 59:
        grade = 'D'
    elif 0 <= student_score <= 49:
        grade = 'F'
    else:
        grade = 'Invalid because of bad Input'
    return grade

#GPA calculator taking dictionary grades
def gpa_calculator(grades):
    grade_total = 0
    length = len(grades)
    for grade in grades.values():
        if grade == 'A':
            score = 4
        elif grade == 'B':
            score = 3
        elif grade == 'C':
            score = 2
        elif grade == 'D':
            score = 1
        else:
            score = 0
        grade_total += score
    return grade_total / length

#add new student
def add_student():
    students = load_data()
    student_id = id_generator(students)
    student_names = set()
    subject_marks = {'AI': 0.0, 'Stat': 0.0, 'Logic': 0.0, 'Programming': 0.0, 'DSA': 0.0}
    subject_grades = {'AI': '', 'Stat': '', 'Logic': '', 'Programming': '', 'DSA': ''}
    keys = subject_marks.keys()
    full_name = input("Enter student name: ")
    if full_name in student_names:
        print("Student already exists")
    gender = input("Enter student gender(Male/Female): ")
    age = int(input("Enter student age: "))
    for key in keys:
        score = float(input(f"Enter Score for {key} out of 100% : "))
        subject_marks[key] = score
        subject_grades[key] = score_to_grade(score)
    average_mark = calculate_average(subject_marks)
    gpa = gpa_calculator(subject_grades)
    students[student_id] = {
        'name': full_name,
        'gender': gender,
        'age': age,
        "average": average_mark,
        'marks': subject_marks,
        'grades': subject_grades,
        'gpa': gpa,
    }
    save_data(students)
    print(f"Student {full_name} has been successfully registered with ID {student_id}")

#generate report card for given student
def generate_report_card():
    print("Generate Report Card")

def view_all_students():
    print("View all Student")

def update_marks():
    print("Update Marks")

def search_student():
    print("Search Students")

def  remove_student():
    print("Remove Student")

def top_performer():
    print("print Top performer student")


def login():
    role = input("Enter role (admin/teacher/student): ").lower()
    name = input("Enter your name: ")
    return role, name

def main_menu():
    print("""
    ==== University Management System ====
    
    Select Role:
    1. Admin
    2. Instructor
    3. Student
    4. Exit Program
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Admin")
    elif choice == "2":
        print("Instructor")
    elif choice == "3":
        print("Student")
    elif choice == "4":
        exit(1)
    else:
        print("Invalid choice. Please Enter again.")


def main():
    main_menu()

main()



