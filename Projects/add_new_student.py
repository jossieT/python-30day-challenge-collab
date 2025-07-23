from datetime import date, datetime
import file_access as fa  
import unique_id_generation as uig
import password_encryption as pe
import degrees_menu as dm

def generate_degree_structure(length_of_years, department:str):
    structure = {
         
            department: {}
        }

    for year in range(1, length_of_years + 1):
        year_key = f"Year {year}"
        structure[department][year_key] = {}

        for semester in range(1, 3):  # Semester 1 and Semester 2
            semester_key = f"Semester {semester}"
            structure[department][year_key][semester_key] = {
                "semester_average": 0,
                "cumulative_average": 0,
                "department": department
            }

    return structure


def new_student():
    data = fa.load_data()

    first_name = input("Enter the student's first name: ").strip().upper()
    second_name = input("Enter the student's second name: ").strip().upper()
    last_name = input("Enter the student's last name: ").strip().upper()
    today = date.today()
    registration_year = today.strftime("%Y-%m-%d")
    birth_date = input("Enter the birth date of student (YYYY-MM-DD): ").strip()

    gender = input("Enter the student's gender: ").strip().upper()
    email = input("Enter the student's email: ").strip().lower()
    nationality = input("Enter the nationality of student:").upper()
    phone_number = input("Enter the phone number of student:").strip()
    address = {
        "region": input("Enter the region of student:").strip().upper(),
        "city": input("Enter the city of student:").strip().upper(),
        "sub_city": input("Enter the sub-city of student:").strip().upper(),
        "woreda": input("Enter the woreda of student:").strip().upper(),
        "kebele": input("Enter the kebele of student:").strip().upper(),
        "house_number": input("Enter the house number of student:").strip().upper(),
        "street": input("Enter the street of student:").strip().upper()
    }

    marital_status = input("Enter the marital status of student:").strip().upper()
    languages = input("Enter the languages spoken by student (comma-separated):").strip().upper().split(",")
    memberships = input("Enter the memberships of student (comma-separated):").strip().upper().split(",")
    scholarship = input("Enter the scholarship status of student:").strip().upper()
    parents = input("Enter the name of student's parents status of student:").strip().upper().split(",")


    contact_info = {
        "first_name_contact_person": input("Enter the contact person's first name:").strip().upper(),
        "last_name_contact_person": input("Enter the contact person's last name:").strip().upper(),
        "phone number": input("Enter the contact person's phone number:").strip(),
        "email": input("Enter the contact person's email:").strip().lower()
    }
    
    student_id =  uig.generate_student_id(first_name, second_name, last_name, registration_year)
    login_credentials = {
        "username": student_id,
        # Default password, must be changed later by the user at the first login
        "password": pe.hash_password(uig.default_student_password())  
    }



    length_of_years, degree_level, department = dm.degrees_menu()
    degree_structure = generate_degree_structure(length_of_years, department)



    # Calculate age based on birth date
    age = datetime.now().year - int(birth_date.split("-")[0])
    school_info = {
        "university_name":input("Which university is the student placed?:"),
        "college": input("What college is he assigned in?:")
    }

    degree = {
        f"{degree_level}": 0
    }
    

    new_student = {
        "student_id": student_id,
        "first_name": first_name,
        "second_name": second_name,
        "last_name": last_name,
        "registration_year": registration_year,
        "school_info": school_info,
        "birth_date": birth_date,
        "age": age,
        "gender": gender,
        "email": email,
        "login_credentials": login_credentials,
        "nationality": nationality,
        "phone_number": phone_number,
        "contact_info": contact_info,
        "address": address,
        "marital_status": marital_status,
        "languages": languages,
        "memberships": memberships,
        "scholarship": scholarship,
        "parents": parents,
        "degrees": degree,
    }

    try:
        # Check if student already exists
                
        if student_id not in data:
            data[student_id] = new_student
        elif student_id in data:
            for info in new_student:
                if info not in data[student_id]:
                    data[student_id][info] = new_student[info]
                else:continue

        else: 
            print("All the information exists.")

        if degree_level not in data[student_id]:
            data[student_id][degree_level] = degree_structure        

        elif department not in data[student_id][degree_level]:
            data[student_id][degree_level][department] = degree_structure

        else:
            print(f"The student is already registered for {degree_level} in {department}")
        data = {student_id: new_student, **data} # Update the data with the new student at the beginning of dictionary
        # Save the updated data
        fa.write_data(data)

        print(f"New student {first_name} {second_name} {last_name} has been added successfully with ID: {student_id}")
    
    except Exception as e:
        print(f"An error occurred while saving the student data: {e}")





