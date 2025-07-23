import file_access as fa
import student_page as sp
import password_encryption as pe
import unique_id_generation as uig
import re
import time
def login():
    try:

        data = fa.load_data()
        
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'

        username = input("Enter your username:").strip()
        password = input("Enter your password:").strip()
        user_password = data.get(username, {}).get("login_credentials", {}).get("password", "")


        if not(pe.check_password(password, user_password)) or username not in data:
            for i in range(5):
                print("❌ Invalid username or password. Please try again.")
                username = input("Enter your username:").strip()
                password = input("Enter your password:").strip()
                if pe.check_password(password, user_password) and username in data:
                    break
                else:
                    if i < 4:
                        print(f"You have only {5-(i+1)} trials remaining.")
                    else:
                        print("❌ Too many failed attempts.")
                        print("🔒 Login is locked for 15 minutes. Please wait...")
                        for remaining in range(15 * 60, 0, -1):

                            mins, secs = divmod(remaining, 60)
                            timer = f"{mins:02d}:{secs:02d}"
                            print(f"⏳ Time remaining: {timer}", end="\r")
                            time.sleep(1)
                        print("\n🔓 You can now try to login again.")
                        return login()
        if pe.check_password(password, user_password) and username in data:
            if pe.check_password(password, user_password) and user_password == uig.default_student_password:
                print("Change your password before proceeding.")
                new_password_1 = input("Enter your new password:").strip()
                new_password_2 = input("Re-enter your new password:").strip()
                while re.match(pattern, new_password_1) and new_password_1 != new_password_2:
                    print("❌ Passwords do not match or invalid format. Please try again.")
                    new_password_1 = input("Enter New Password:").strip()
                    new_password_2 = input("Confirm New Password:").strip()
                if re.match(pattern, new_password_1) and new_password_1 == new_password_2:
                    data[username]["login_credentials"]["password"] = pe.hash_password(new_password_1)
                    fa.write_data(data)
                    print("Password changed successfully.")
            
        else:
            print("Login unsuccessful.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def log_out():
    try:

        click_on_logout = input('Enter Y or y to logout or N or n to stay on the page:')
        if click_on_logout == 'y':
            print("Are you sure you want to logout Y/N?:")
            if click_on_logout.lower() == 'y':
                return exit()
        else:
            sp.student_main_menu()
            
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
