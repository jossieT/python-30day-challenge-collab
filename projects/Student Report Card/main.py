
def add_student():
    print("Add Student page")

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

def student_view():
    while True:
        print("""
        1. View My Report Card
        2. Back to Main Menu / Logout
        3. Exit program
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            generate_report_card()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def login():
    role = input("Enter role (admin/teacher/student): ").lower()
    name = input("Enter your name: ")
    return role, name

def teachers_admin_view():
    while True:
        print("Welcome, Admin/Teacher!")
        print("""
        1. Add New Student
        2. Generate Report Card
        3. View All Students
        4. Search Student
        5. Update Marks
        6. Remove Student
        7. Top Performer
        8. Exit
        """)
        print("Please select an option (1-8):")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            generate_report_card()
        elif choice == "3":
            view_all_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            update_marks()
        elif choice == "6":
            remove_student()
        elif choice == "7":
            top_performer()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    role, username = login()
    if role == "student":
        student_view()
    else:
        teachers_admin_view()

main()



