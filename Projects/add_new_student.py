from datetime import datetime
import file_access as fa  
import unique_id_generation as uig
import password_encryption as pe

def new_student():

    first_name = input("Enter the student's first name: ").strip().upper()
    second_name = input("Enter the student's second name: ").strip().upper()
    last_name = input("Enter the student's last name: ").strip().upper()
    registration_year = input("Enter the student's registration year (e.g., 2025): ").strip()
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
    degree_level = input("For which degree level is the student registering for (e.g., bachelor of science?")

    # Calculate age based on birth date
    age = datetime.now().year - int(birth_date.split("-")[0])
    school_info = {
        "university_name":input("Which university is the student placed?:"),
        "college": input("What college is he assigned in?:")
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
        "degree_level":[degree_level]

    }

    data = fa.load_data()
    if student_id not in data:
            data[student_id] = new_student
    else: 
         print("The student id exists.")

    fa.write_data(data)


