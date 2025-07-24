import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        return []

def save_data(filepath, data):
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error Saving data to {filepath}: {e}")

def append_data(filepath, new_data):
    data = load_data(filepath)
    data.append(new_data)
    save_data(filepath, data)

def find_by_id(filepath, item_id):
    data = load_data(filepath)
    for item in data:
        if item.get('id') == item_id:
            return item
    return None