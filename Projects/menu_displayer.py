import os
def main_menu():
    print("#"*150)
    print("##" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t0. Save and Exit\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t1. Go To Main Menu\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t2. Add New Student\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t3. Add Subjects\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t4. Generate Report Card\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t5. Remove The Student Record\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t6. View Student Records\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t7. Search For Student\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t8. Edit The Score \t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t9. Search For Student\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t10. Clear The Screen\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("##" + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    
    print("#"*150)
    

def display_menu():
    signal = ""
    
    while signal.lower() != 'done':
            signal = input("What do you want to do?")
            if signal == "1":
                main_menu()
            elif signal == "2":
                print("Add new student")
            elif signal == "clear".lower():
                if os.name == 'nt':
                    os.system('cls')
                 
            else:
                exit()
    else:
        exit()


if __name__ == "__main__":
    display_menu()