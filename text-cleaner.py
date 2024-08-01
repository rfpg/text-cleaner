import re

# Path to the original file
file_path = 'file.txt'
# Path for the cleaned output
output_path = 'cleaned_file.txt'

# Define a function to determine if a line starts with a timestamp
def starts_with_timestamp(line):
    return re.match(r'\d{2}:\d{2}:\d{2};\d{2}\s*\d{2}:\d{2}:\d{2};\d{2}', line)

# Read the original file
with open(file_path, 'r') as file:
    text = file.read()

# Split into lines and process each line
cleaned_text = ''
lines = text.split('\n')

for i in range(len(lines)):
    # Remove ">>" and extra whitespace from the line first
    line = re.sub(r'>>', '', lines[i])
    line = re.sub(r'\s+', ' ', line).strip()

    if starts_with_timestamp(line):
        # Start a new line with a timestamp, unless it's the very first line
        if cleaned_text:
            cleaned_text += '\n'
        cleaned_text += line
    else:
        # Continue on the same line if there's no timestamp
        cleaned_text += ' ' + line

# Ensure no leading/trailing spaces
cleaned_text = cleaned_text.strip()

# Write the cleaned text to a new file
with open(output_path, 'w') as file:
    file.write(cleaned_text)

print("File cleaned and saved to:", output_path)
