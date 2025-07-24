from file_handler import load_data, save_data, append_data

def add_new_student():
    students = load_data()
    student_id = id_generator(students)

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