# File Read & Write Challenge

# Open the original file for reading
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (example: make uppercase)
modified_content = content.upper()

# Write modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File successfully modified and saved to output.txt ✅")

# Error Handling Lab

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
