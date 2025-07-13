import random
import os

def generate_student_id(first_name, second_name, last_name):
    # Ensure names are long enough
    if len(first_name) < 1 or len(second_name) < 2 or len(last_name) < 3:
        return "Invalid name lengths"

    id_part = first_name[0] + second_name[1] + last_name[2]
    random_number = f"{random.randint(0, 999):03}"  # 3-digit padded
    student_id = id_part.upper() + random_number
    return student_id
