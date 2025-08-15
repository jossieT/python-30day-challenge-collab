def show_student_menu():
    while True:
        print("""
        ---- Student Panel ----
              
        1. View My Profile
        2. View Enrolled Courses
        3. View Grades
        4. Logout
        
        """)
        choice = input("Enter choice: ")

        if choice == "1":
            print("View My Profile")
        if choice == "2":
            print("View Enrolled Courses")
        if choice == "3":
            print("View Grades")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

show_student_menu()