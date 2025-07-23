import os
import add_new_student as ans
def admin_menu():
    print("#"*150)
    print("##" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t1. Save and Exit\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t2. Go To Main Menu\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t3. Add New Student\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t4. Remove The Student Record\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t5. View Student Records\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t6. Search For Student\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t7. Edit The Score \t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t8. Clear The Screen\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    
    print("#"*150)

def teacher_menu():
    print("#"*150)
    print("##" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t1. Go To Main Menu\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t2. View Student Records\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t3. Search For Student\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t4. Generate The Student Report\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    
    print("##" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    
    print("#"*150)

def student_menu():
    print("#"*150)
    print("##" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t1. Go To Main Menu\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t2. View Student Records\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t3. Search For Student\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t4. Generate Your Report\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t5. Print Course Checklist \t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    
    print("#"*150)
    

def display_menu():
    signal = ""
    
    while signal.lower() != 'done':
            signal = input("What do you want to do?")
            if signal == "1":
                admin_menu()
            elif signal == "2":
                ans.new_student()
            elif signal == "3":
                pass
            elif signal == "4":
                pass
            elif signal == "5":
                pass
            elif signal == "6":
                pass
            elif signal == "7":
                pass
            elif signal == "8":
                pass
            elif signal == "0":
                pass
            elif signal == "clear".lower():
                if os.name == 'nt':
                    os.system('cls')
                 
            else:
                exit()


if __name__ == "__main__":
    display_menu()