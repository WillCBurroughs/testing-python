def main():
    while True:
        user_input = input("What would you like to do? 1. (quit) 2. (read) file 3. (write) file ")

        if user_input.lower() == 'write':
            file_name = input("What would you like to name this file? ")
            text_to_write = input("What text would you like to write? ")
            write_file_with_text(file_name, text_to_write)  
        elif user_input.lower() == "read":
            file_name = input("What file would you like to read? ")
            open_file_and_read(file_name)
        elif user_input.lower() == "quit":
            break 
        else:
            print("Invalid input, try again")

def open_file_and_read(file_name):
    try:
        with open(file_name, 'r') as fhand:  # Use 'with' to ensure the file is properly closed
            print(fhand.read())
    except FileNotFoundError:  # Specific exception for file not found
        print("Invalid file name")
    except Exception as e:  # Catch-all for other exceptions
        print("Something went wrong:", e)

def write_file_with_text(file_name, file_information):
    try:
        with open(file_name, "w") as fhand:  # Use 'with' to ensure the file is properly closed
            fhand.write(file_information)
    except Exception as e:  # Catch-all for exceptions
        print("Something went wrong:", e)

if __name__ == "__main__":
    main()