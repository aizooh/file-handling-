def modify_file_content(content):
    """
    Modify the file content.
    For demo purposes, we'll convert it to uppercase.
    """
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening the input file
        with open(filename, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Write to a new file
        output_filename = "modified_" + filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"❌ Error: Could not read from or write to the file.")

if __name__ == "__main__":
    main()
