import json

# Load the input JSON file
with open('output_json_file.json', 'r') as file:
    data_list = json.load(file)

# Convert the data
converted_data = []
for data in data_list:
    converted_item = {
        "id": data["inscriptionId"],
        "meta": {
            "name": data["name"],
            "attributes": [
                {"trait_type": k, "value": v}
                for k, v in data["attributes"].items()
            ]
        }
    }
    converted_data.append(converted_item)

# Save the converted data to a new JSON file
with open('OW.json', 'w') as file:
    json.dump(converted_data, file, indent=2)

print("Conversion complete. Check output.json for the result.")
