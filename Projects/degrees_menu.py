from tabulate import tabulate
import file_access as fa
def degrees_menu():
    try:
        data = fa.load_data()
        degree_programs = data["degree programs"]
        

    # Gather rows into a list of [Program, Field, Years]
        rows = []
        counter = 1
        for program, fields in degree_programs.items():
            for field, years in fields.items():
                rows.append([counter, program, field, years])
                counter += 1

        # Print as table
        print(tabulate(rows, headers=["Program", "Field of Study", "Years"], tablefmt="simple"))

        print("Select a program by entering the corresponding number:")
        
        choice = int(input())
        if 1 <= choice <= len(rows):
            selected_program = rows[choice - 1]
            print(f"You selected: {selected_program[1]} in {selected_program[2]} for {selected_program[3]} years.")
            length_of_years = selected_program[3]
            degree_level = selected_program[1]
            department = selected_program[2]
            return length_of_years, degree_level, department
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")




