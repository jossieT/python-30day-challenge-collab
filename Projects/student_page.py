import file_access as fa
from datetime import datetime
def student_main_menu():
    pass
def view_records():
    pass
def course_registration(username):
    data = fa.load_data()
    # Replace with your actual start date
    course_start_date = input("Enter the course start date (YYYY-MM-DD): ").strip()
    year, month, day = map(int, course_start_date.split('-'))
    start_date = datetime(year, month, day)
    today = datetime.today()

    # Calculate number of months
    months = (today.year - start_date.year) * 12 + (today.month - start_date.month)

    # Optionally: include partial month if today is past the start day
    if today.day >= start_date.day:
        months += 1
    
    if months >= 5:

        year = input("Enter the year you want to register for courses (e.g., 1): ").strip().upper()
        year_ = "Year " + year 
        semester = input("Enter the semester you want to register for courses (e.g., 1): ").strip().upper()
        semester_ = "semester " + semester
        courses = data[username]["courses_completed"][year_]
        if year_ not in courses:
            print(f"No courses available for {year_}.")
            return
        if semester_ not in courses[year_]:
            print(f"No courses available for {year_} {semester_}.")
            return
        print(f"Available courses for {year_} {semester_}:")
        for course, details in data["SECE"][year_][semester_]:
            print(f"{course}: {details['ects']} ECTS")
        
        if year == "1" and semester == "1" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "1" and semester == "2" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "2" and semester == "1" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "2" and semester == "2" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "3" and semester == "1" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "3" and semester == "2" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "4" and semester == "1" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "4" and semester == "2" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "5" and semester == "1" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        elif year == "5" and semester == "2" and len(courses[year_][semester_]) == 0:
            data[username]['courses_completed'][year_][semester_] = data["SECE"][year_][semester_]
        else:
            print("You have already registered for all courses.")
    else:
        print("You haven't finished the previous semester. Due to this courses for the next semester are not available.")
