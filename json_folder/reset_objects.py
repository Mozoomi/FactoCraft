import json

def replace_json_content(source_file, replacement_file):
    # Read the contents of the replacement JSON file
    with open(replacement_file, 'r') as file:
        replacement_data = json.load(file)

    # Write the contents of the replacement JSON file to the source JSON file
    with open(source_file, 'w') as file:
        json.dump(replacement_data, file, indent=4)  # You can specify the indentation level as needed

if __name__ == "__main__":
    replace_json_content('json_folder/gameObjects.json', 'json_folder/base_gameObjects.json')
    print("GAME OBJECT: RESET")