import file_access as fa
import password_encryption as pe
def register_for_courses(username):
    data = fa.load_data()
    
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
    for course, details in data[username]["courses_aait_sece"][year_][semester_]:
        print(f"{course}: {details['ects']} ECTS")
    
    if year == "1" and semester == "1" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "1" and semester == "2" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "2" and semester == "1" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "2" and semester == "2" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "3" and semester == "1" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "3" and semester == "2" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "4" and semester == "1" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "4" and semester == "2" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "5" and semester == "1" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    elif year == "5" and semester == "2" and len(courses[year_][semester_]) == 0:
        data[username]['courses_completed'][year_][semester_] = data[username]["courses_aait_sece"][year_][semester_]
    else:
        print("You have already registered for all courses.")
def login():
    username = input("Enter your username:")
    password = input("Enter you password:")
    data = fa.load_data()
    login_access = data["login_credentials"]
    if username in data and username == login_access["username"] and pe.check_password(password, login_access["password"]):
        register_for_courses(username)
    else:
        print("Invalid username or password. Please try again.")
        login()
