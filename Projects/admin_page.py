import file_access as fa
import add_new_student as ans
import password_encryption as pe
def remove_student_record():
    data = fa.load_data()
    student_id = input("Enter student ID that you want to remove:")
    username = input("Enter your username:"), password = input("Enter your password:")
    if student_id in data:
        if username == data["admin"][username] and pe.check_password(password, data["admin"][username]["password"]):
            del data[student_id]
    else:
        print(f"The student with ID {student_id} does not exist.")

def add_student():
   data = fa.load_data()
   username = input("Enter your username:"), password = input("Enter your password:")
   if username == data["admin"][username] and pe.check_password(password, data["admin"][username]["password"]):
       ans.new_student()

        



