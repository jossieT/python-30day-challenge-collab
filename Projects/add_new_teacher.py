import file_access as fa
import menu_displayer as md
from datetime import datetime
import degrees_menu as dm
def generate_unique_email(first_name, last_name, existing_emails, domain="aau.edu.et"):
    base_email = f"{first_name.lower()}.{last_name.lower()}@{domain}"
    
    # If base email is not taken, return it
    if base_email not in existing_emails:
        return base_email
    
    # Try appending numbers until a unique email is found
    counter = 1
    while True:
        new_email = f"{first_name.lower()}.{last_name.lower()}{counter}@{domain}"
        if new_email not in existing_emails:
            return new_email
        counter += 1

def add_new_teacher():
    # Load existing emails from the JSON file
    data = fa.load_data()
    now = datetime.now()
    existing_emails = data["teachers"]["existing_emails"]
    first_name = input("Enter the teacher's first name: ").strip()
    last_name = input("Enter the teacher's last name: ").strip()
    courses_to_teach = input("Enter the courses to teach (comma separated): ").strip().split(',')
    courses_to_teach = [course.strip() for course in courses_to_teach if course.strip()]
    assignment_year = now.strftime("%Y-%m-%d")
    department = input("Enter department:")
    # Generate a unique email for the new teacher
    email = generate_unique_email(first_name, last_name, existing_emails)

    teachers = data.get("teachers", {}).get("department", {})
  
    # Create the new teacher's data
    degree_information = {
                   "Bachelor of Science": {
                       "university": '',
                       "specialization": "",
                       "thesis": "",
                       "year_of_study": ""
                   },
                    "Masters Degree": {
                        "university": "",
                        "specialization": "",
                        "research": "",
                        "year_of_study": ""
                    },
                    "PhD": {
                        "university": "",
                        "specialization": "",
                        "dissertation": "",
                        "year_of_study": ""
                    }
                }
    new_teacher = {
        "first_name": first_name,
        "last_name": last_name,
        "username": email,
        "password": "$2b$12$uG0vcQ6V60MrzhK9TuYEhe.gVSUN1bxrTz4hdoD63gykw7eEzvQ0u",  # Example password, should be hashed in practice
        "courses_to_teach": courses_to_teach,
        "start_year": assignment_year,
        "degree_information": degree_information
    }


    if new_teacher not in teachers:
        data["teachers"][department][email] = new_teacher
        fa.write_data()

    
def add_information(username):
    data = fa.load_data()
    menu_items = [
        "1. Exit The System",
        "2. Bachelor of Science {University, Research Thesis, Years of Study (e.g., 2025-2027),Research Interests}",
        "3. Masters Degree {University, Research Thesis, Years of Study (e.g., 2025-2027),Research Interests}",
        "4. PhD {University, Research Thesis, Years of Study (e.g., 2025-2027),Research Interests}",
        "5. Research Interest"
    ]

    input_dictionary = {
        2: "Bachelor of Science",
        3: "Master of Science",
        4: "PhD",
    }

    md.main_menu(menu_items)
    department = input("Enter your department:")
    menu_number = ""
    if username in data.get("teachers", {}).get(department, {}):
        
        while menu_number.lower() != "done":
            menu_number = input("Enter a number from the above menu:").strip()
            if menu_number == "1":
                return
            else:
                if int(menu_items) in input_dictionary:
                    data["teachers"][department][username]["degree_information"][input_dictionary[int(menu_number)]] = {
                        "university": input("University Name:"),
                        "specialization": input("Specialization"),
                        "thesis": input("Resear Title:"),
                        "year_of_study": input("Start Year - Final Year:")
                    }
                elif menu_number == 5:
                    research_interest = input("Research Interests Separated by Comma:").capitalize().split(',')
                    data["teachers"][department][username]["research_interests"] = research_interest
                
                else:
                    print("Invalid Option! Please try again.")
                    return
            fa.write_data()
    else:
        print("Invalid Username!")


                

        
            
            
        
    
    

