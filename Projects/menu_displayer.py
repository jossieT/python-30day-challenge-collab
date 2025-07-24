import os
import add_new_student as ans
import os
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset color after each print

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu(menu_items:list):
    clear_screen() # Clear the screen before displaying the menu
    width = 60
    border = "#"
    print(Fore.CYAN + border * width)

    for i, item in enumerate(menu_items, start=1):
        line = f"{Fore.YELLOW}{i:>10}. {Fore.MAGENTA}{item[3:]}"  # Right-align number, reuse item text
        print(Fore.CYAN + border + " " + line.ljust(width + 7) + Fore.CYAN + border)  # Left-justified

    print(Fore.CYAN + border * width)


def admin_menu():
    menu_items = [
        "1. Save and Exit",
        "2. Go To Main Menu",
        "3. Add New Student",
        "4. Remove The Student Record",
        "5. View Student Records",
        "6. Search For Student",
        "7. Edit The Score",
        "8. Clear The Screen"
    ]
    main_menu(menu_items)

def teacher_menu():
    menu_items = [
        "1. Go To Main Menu",
        "2. View Student Records",
        "3. Search For Student",
        "4. Generate The Student Report"
    ]
    main_menu(menu_items)
def student_menu():
    menu_items = [
        "1. Go To Main Menu",
        "2. View Student Records",
        "3. Search For Student",
        "4. Generate Your Report",
        "5. Print Course Checklist"
    ]
    main_menu(menu_items)
    

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

