import json

# Load the first JSON file
with open('folder59.json', 'r') as file:
    first_json = json.load(file)

# Load the second JSON file
with open('Anti_doginaldogsDM.json', 'r') as file:
    second_json = json.load(file)

# Initialize the new JSON dictionary
new_json = {}

# Extract the number from the filename and match it with the second JSON
for filename, data in first_json.items():
    number = int(filename.split('AntiDoginalDog')[1].split('.html')[0])
    
    # Find the corresponding entry in the second JSON based on the number
    for entry in second_json:
        name = entry["name"]
        entry_number = int(name.split('#')[1])
        if entry_number == number:
            new_json[filename] = {
                "txid": data["txid"],
                **entry
            }
            break

# Save the new JSON to a file
with open('folder_json_file.json', 'w') as file:
    json.dump(new_json, file, indent=4)

print("New JSON file has been created successfully.")
