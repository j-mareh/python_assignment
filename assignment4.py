# file_handler.py
# 📂 A simple file processing program with error handling
# Reads a file, modifies its content, and writes to a new file

def process_file():
    # Ask user for input and output filenames
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")

    try:
        # Try to open and read the input file
        with open(input_file, "r") as infile:
            content = infile.read()
            print("\n✅ File read successfully!\n")

        # Modify content (example: convert text to uppercase)
        modified_content = content.upper()

        # Write modified content to the chosen output file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"🎉 File processed successfully! Modified content saved in '{output_file}'")

    except FileNotFoundError:
        print("❌ Error: The input file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read/write this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    process_file()


