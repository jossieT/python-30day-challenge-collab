import bcrypt

def hash_password(password: str) -> str:
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password: str, hashed: str) -> bool:
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


if __name__ == "__main__":
    # Example usage
    password = "Admin@1832"
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)
    is_correct = check_password("Admin@1832", hashed_password)
    print("Password is correct:", is_correct)