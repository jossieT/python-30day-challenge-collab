import file_access as fa
import student_page as sp
import password_encryption as pe
import unique_id_generation as uig
import re
import time
def login():

    data = fa.load_data()
    
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'

    username = input("Enter your username:").strip()
    password = input("Enter your password:").strip()
    user_password = data.get(username, {}).get("login_credentials", {}).get("password", "")

    if not(pe.check_password(password, user_password)) or username not in data:
        for i in range(5):
            print("❌ Invalid username or password. Please try again.")
            username = input("Enter your username:").strip().upper()
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
    else:
        print("Login successful.")


if __name__ == "__main__":
    login()