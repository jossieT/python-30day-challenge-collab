def show_instructor_menu():
    while True:
        print(""" 
        ---- Instructor Menu ----
        
        1. View My Courses
        2. View Enrolled Students in a course
        3. Assign Grades to Students
        4. Update Course Info
        5. Logout
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("View My Courses")
        elif choice == "2":
            print("View Enrolled Students in a course")
        elif choice == "3":
            print("Assign Grades to Students")
        elif choice == "4":
            print("Update Course Info")
        elif choice == "5":
            break
        else:
            print("Invalid Choice")
show_instructor_menu()