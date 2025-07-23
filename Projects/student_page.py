import file_access as fa
from datetime import datetime
import degrees_menu as dm

def student_main_menu():
    pass
def course_registration(username):
    try:
        data = fa.load_data()
        maximum_ects_per_semester = 37
        length_of_years, degree_level, department = dm.degrees_menu()
        courses = data[department]["courses"][degree_level]
        degree = data[username]["degrees"]
        dropped_courses = data[username]["dropped_courses"]
        if degree[degree_level] != 0:
            print(f"You have completed {degree_level} in {department}."
                  f"from {data[username]['school_info']['university_name']}.")
        elif degree_level in data[username]:
            if department in data[username][degree_level]:
                for i in range(1, length_of_years + 1):
                    year_keys = "Year " + 1
                    for i in range(1, 3):
                        semester = "Semester " + i
                        semester_data = data[username][degree_level][department][year_keys][semester]
                        for course in courses[year_keys][semester]:
                            if semester_data["semester_average"] == 0 and course not in semester_data:
                                semester_data[course] = courses[year_keys][semester][course]
                                
                                




    except Exception as e:
        print(f"The error occurred: {e}")


def add_course():
    pass

def drop_course():
    pass
