import random
import degrees_menu as dm
import file_access as fa
def generate_student_id(degree_level, type_of_registration, current_year):
   
    try:
        student_data = fa.load_data()
        existing_ids = student_data.get("student_id", [])

        # If all 9000 possible 4-digit numbers are used, raise an error
        if len(existing_ids) >= 9000:
            raise ValueError("All possible 4-digit IDs are used.")

        # Generate a unique new ID
        while True:
            new_id = random.randint(1000, 9999)
            if new_id not in existing_ids:
                break  # Unique ID found

        # Save the ID
        student_data.setdefault("student_id", []).append(new_id)

        # Format based on degree level and registration type
        if degree_level in student_data.get("bachelor of science", []):
            prefix = "BSR" if type_of_registration == "Regular" else "BSE"
        elif degree_level in student_data.get("Masters Degrees", []):
            prefix = "MSR" if type_of_registration == "Regular" else "MSE"
        elif degree_level in student_data.get("PhD", []):
            prefix = "PDR" if type_of_registration == "Regular" else "PDE"
        else:
            raise ValueError("Invalid degree level.")

        return f"{prefix}/{new_id:04d}/{current_year}"

    except ValueError as e:
        print(f"Error: {e}")
        return None

def default_student_password() -> str:
    return "Welcome2aau"



