import random
def generate_student_id(first_name, second_name, last_name, registration_year):
    # Ensure names are long enough
    if len(first_name) < 1 or len(second_name) < 1 or len(last_name) < 1:
        return "Invalid name lengths"

    start_of_id:str = first_name[0] + second_name[0] + last_name[0] 
    # Generate 4 unique digits (0-9)
    unique_digits = random.sample(range(10), 4)

    # Convert to a single string
    middle_of_id = ''.join(str(digit) for digit in unique_digits)

    year = registration_year.strip().split("-")[0]

    last_of_id = registration_year[-2] + registration_year[-1]
    student_id = start_of_id.upper() + "/" + middle_of_id + "/" + last_of_id
    return student_id
def default_student_password() -> str:
    return "Welcome2aau"



