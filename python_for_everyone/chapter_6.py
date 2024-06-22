def main():
    while True: 
        test_word = input("What word or sentence would you like? ")
        # Will end if done
        if validate_input(test_word):
            break

        test_character = input("What letter would you like to count? ")

        occurences = check_for_input(test_character, test_word)
        print(f"{test_character} appeared {occurences} times in {test_word} ")

def check_for_input(test_character, test_word):
    count_letter = 0
    for letter in test_word:
        if letter == test_character:
            count_letter += 1 
    return count_letter

def validate_input(test_word):
    if test_word.lower() == "done":
        return True
    return False

if __name__ == "__main__":
    main()