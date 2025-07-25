import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.file_handler import load_data, append_data, save_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRACKER_FILE = os.path.join(BASE_DIR, '..', 'data', 'tracker.json')

def id_generator(entity_type, year):
    tracker = load_data(TRACKER_FILE)  # list of dicts
    key = f"{entity_type.upper()}{year}"

    # Get the last dict in the list or create a new one
    last_record = tracker[-1] if tracker else {}

    # Get the last index for this key, default to 0
    last_index = last_record.get(key, 0)

    # Increment the index
    new_index = last_index + 1

    # Update the key in the last record
    last_record[key] = new_index

    # If tracker was empty, append new record
    if not tracker:
        tracker.append(last_record)
    else:
        tracker[-1] = last_record

    # Save the updated tracker list (not just one dict!)
    save_data(TRACKER_FILE, tracker)

    return f"{key}-{new_index:03d}"
