
def main():
    passed_in_values = input("What would you like to test? ")
    hold_output = which_letters_in_string(passed_in_values)
    print(hold_output)
    print("Your word/s had", how_many_unique_letters(hold_output), "unique letters")


def which_letters_in_string(passed_in_words):
    return_values = set()
    for letter in passed_in_words:
        return_values.add(letter)
    return sorted(return_values)

def how_many_unique_letters(passed_in_set):
    return len(passed_in_set)

if __name__ == "__main__":
    main()