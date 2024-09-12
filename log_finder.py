def find_error_lines(file_path, error_string, log_file):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

        # Initialize variables
        matching_lines = []
        line_number = 1

        # Iterate through each line
        for line in lines:
            # Check if the error string is in the line
            if error_string.lower() in line.lower():
                # If found, add the line number and the line itself to the list
                matching_lines.append(f"Line {line_number}: {line.strip()}")

            # Increment line number
            line_number += 1

        # Print the matching lines
        if matching_lines:
            print(f"Found '{error_string}' in the following lines:")
            for line in matching_lines:
                print(line)

            # Save findings to log.txt
            with open(log_file, "a") as log_file:
                
                for line in matching_lines:
                    log_file.write(line + "\n")

            print("\nFindings saved to log.txt")
        else:
            print(f"No occurrences of '{error_string}' found in the file.")
            print("No log file created.")

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage example
file_path = "manish.txt"  # Replace this with your actual file path
log_file = input("Enter the file name in which you want to store the logs : ")
error_string = input("Enter the error string to search for: ")

find_error_lines(file_path, error_string, log_file)
