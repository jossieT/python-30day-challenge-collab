import file_access as fa
def search_student():
    data = fa.load_data()
    try:
        search_year  = input("Which year's report you want to view (e.g., 1)?\n")
        student_id = input("What is the student's ID:").upper()
        search_semester = input("Which semester record you want to view (e.g., 1)?\n ")
        year = "Year " + search_year
        semester = "Semester " + search_semester
        search_result = data[student_id]["courses_completed"][year][semester]
        print("Search results for student ID:", student_id)
        for course, values in search_result.items():
            print(f"{course}\t\t\t {values}")
        else:
            print("Record not found.")
    except:
        print("Record not found.")



