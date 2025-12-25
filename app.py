import json
import glob
import os

# Define the path to your files
path_to_files = r'scancode-licensedb-main\docs'
output_file = 'dataset.json'

merged_data = []

# Loop through all .json files in the directory
# Using os.path.join for cross-platform compatibility
for filename in glob.glob(os.path.join(path_to_files, '*.json')):
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            merged_data.append(data)
        except json.JSONDecodeError:
            print(f"Error skipping invalid JSON: {filename}")

# Save the combined list to a new file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, indent=4)

print(f"Successfully merged {len(merged_data)} files into {output_file}")