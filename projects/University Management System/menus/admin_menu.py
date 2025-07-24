def show_admin_menu():
    while True:
        print("""
        ---- Admin Panel ----
        
        1. Add New Student
        2. View All Students
        3. Manage Courses
        4. Logout
        """)
        print("Please select an option (1-4):")
        choice = input("Enter choice: ")

        if choice == "1":
            print("Add New Student")
        elif choice == "2":
            print("View All Students")
        elif choice == "3":
            print("Manage Courses")
        elif choice == "4":
            print("Logout")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
show_admin_menu()