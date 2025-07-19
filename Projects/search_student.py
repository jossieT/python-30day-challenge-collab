import file_access as fa

def search_student():

    data = fa.load_data()
    
    try:
        student_id = input("What is the student's ID:").upper()
        courses_completed = data[student_id]['courses_completed']
        # Display in ascending order from final year semester 2 down to year 1 semester 1
        for year in sorted(courses_completed.keys(), reverse=True):
            semesters = courses_completed[year]
            for semester in sorted(semesters.keys(), reverse=True):
                print(f"\n{year} - {semester}")
                print(f"Department: {semesters[semester].get('department', '')}")
                print(f"Semester Average: {semesters[semester].get('semester_average', '')}")
                print(f"Cumulative Average: {semesters[semester].get('cumulative_average', '')}")
                print(f"{'Course':40} {'Score':>10} {'Grade':>10} {'ECTS':>10}")
                print("-" * 75)
                for course, details in semesters[semester].items():
                    if course in ["semester_average", "cumulative_average", "department"]:
                        continue
                    print(f"{course:40} {details['score']:>10} {details['grade']:>10} {details['ects']:>10}")
    except KeyError:
        print("Record not found.")




