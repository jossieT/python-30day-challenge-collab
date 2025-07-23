import file_access as fa
import student_page as sp
import password_encryption as pe
import re
def login():

    pattern = r'^(?=.*[^A-Za-z0-9]).{8,}$'

    password = input("Enter your password (at least 8 characters, including a special character): ")

    if re.match(pattern, password):
        print("✅ Valid password")
    else:
        print("❌ Invalid password")


    username = input("Enter your username:")
    password = input("Enter you password:")
    data = fa.load_data()
    login_access = data[username]["login_credentials"]
    if username in data and username == login_access["username"] and pe.check_password(password, login_access["password"]):
        sp.course_registration(username)
    else:
        print("Invalid username or password. Please try again.")
        login()
def log_out():
    click_on_logout = input('Enter Y or y to logout or N or n to stay on the page:')
    if click_on_logout == 'y':
        print("Are you sure you want to logout Y/N?:")
        if click_on_logout.lower() == 'y':
            return exit()
    else:
        sp.student_main_menu()
