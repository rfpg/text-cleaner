import re

# Path to the original file
file_path = 'file.txt'
# Path for the cleaned output
output_path = 'cleaned_file.txt'

def is_timestamp(line):
    return bool(re.match(r'\d{2}:\d{2}:\d{2};\d{2}\s*\d{2}:\d{2}:\d{2};\d{2}', line))

# Read the original file
with open(file_path, 'r') as file:
    text = file.read()

# Split into lines and process each line
cleaned_text = ''
lines = text.split('\n')
for line in lines:
    line = line.strip()
    # Remove all ">>" and ">> " before further processing
    line = re.sub(r'>>\s*', '', line)

    # Check if the line starts with a timestamp
    if is_timestamp(line):
        # Split the timestamp from the rest of the line
        parts = re.split(r'(\d{2}:\d{2}:\d{2};\d{2}\s*\d{2}:\d{2}:\d{2};\d{2})', line, 1)
        timestamp = parts[1]
        text_part = parts[2].strip()

        # Check if the text part starts with a lowercase letter
        if text_part and text_part[0].islower():
            # Skip adding this timestamp and its text part
            continue

        # Add the timestamp and the text part on separate lines, followed by an extra newline
        cleaned_text += timestamp + '\n\n' + text_part + '\n\n'
    else:
        # This handles lines that don't start with a timestamp, appending them to the last text
        if cleaned_text.endswith('\n\n'):
            cleaned_text = cleaned_text.rstrip('\n\n') + ' '
        cleaned_text += line + '\n\n'

# Ensure no trailing newlines
cleaned_text = cleaned_text.strip()

# Write the cleaned text to a new file
with open(output_path, 'w') as file:
    file.write(cleaned_text)

print("File cleaned and saved to:", output_path)
