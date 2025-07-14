import json
file_path = "D:\python-30day-challenge-collab\Projects\student_list.json"
def load_data():
    # Open and load the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Function to generate a student ID based on names
    return data

def write_data(student_data):
     with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(student_data, file, indent=4)