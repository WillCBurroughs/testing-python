
def main():
    print("Hello: ", end="")
    user_greeting = input()
    print(checkInput(user_greeting))

# Need to get user input, need to check if first word is hello if not, does it start with h, else return 0 
# Get user input, check first word 
# Check first letter 

def checkInput(test_input):
    # Removing blank spaces, putting to lower
    test_input = test_input.strip().lower()
    if test_input[0:5] == "hello":
        return "$0"
    elif test_input[0] == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()