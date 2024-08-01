import re

# Path to the original file
file_path = 'file.txt'
# Path for the cleaned output
output_path = 'cleaned_file.txt'

# Read the original file
with open(file_path, 'r') as file:
    text = file.read()

# Remove timestamps
cleaned_text = re.sub(r'\d{2}:\d{2}:\d{2};\d{2}\s*\d{2}:\d{2}:\d{2};\d{2}', '', text)

# Remove ">>" characters
cleaned_text = re.sub(r'>>', '', cleaned_text)

# Remove excess whitespace
cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

# Write the cleaned text to a new file
with open(output_path, 'w') as file:
    file.write(cleaned_text)

print("File cleaned and saved to:", output_path)
