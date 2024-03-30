import json
from typing import Dict


# Load initial data from JSON file
with open("test.json", "r") as file:
    all_data = json.load(file)


# Helper function to save data back to JSON file
def save_data(data: Dict):
    with open("test.json", "w") as file:
        json.dump(data, file, indent=2)