import os
import json
import re

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

def merge_json_files(directory):
    merged_data = {}

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if isinstance(data, dict):
                        merged_data.update(data)
                    else:
                        print(f"Skipping {filename}: not a dictionary")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from file {filename}: {e}")
            except UnicodeDecodeError as e:
                print(f"Encoding error in file {filename}: {e}")
            except Exception as e:
                print(f"Unexpected error with file {filename}: {e}")

    sorted_merged_data = dict(sorted(merged_data.items(), key=lambda item: extract_number(item[0])))
    
    with open("merged_sorted.json", 'w', encoding='utf-8') as outfile:
        json.dump(sorted_merged_data, outfile, indent=4)

# Change the current working directory as needed
merge_json_files('.')
