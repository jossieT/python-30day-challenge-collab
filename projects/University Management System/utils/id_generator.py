import os

from file_handler import load_data, append_data, save_data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRACKER_FILE = os.path.join(BASE_DIR, '..', 'data', 'tracker.json')
def id_generator(entity_type, year):
    tracker = load_data(TRACKER_FILE)
    # Ensure it's a dictionary
    if not isinstance(tracker, dict):
        tracker = {}
    key = f"{entity_type.upper()}{year}"
    tracker[key] = tracker.get(key, 0) + 1
    save_data(TRACKER_FILE, tracker)

    return f"{key}-{tracker[key]:03d}"

print(id_generator("STUD", 2025))