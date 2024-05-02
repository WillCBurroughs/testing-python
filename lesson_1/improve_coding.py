import random

INCORRECT_ANSWERS = ["A byte has 2 units of memory", "There are 3 possible values of a boolean"]
CORRECT_ANSWERS = ["Python, Javascript and Java are all programming languages", "Assembling code means turning assembly code into machine readable code"]

def generate_question():
    correct_index = random.randint(0, 1)
    incorrect_indices = [0, 1]  # Indices for the incorrect answers
    incorrect_indices.remove(correct_index)  # Remove the index used for correct answer
    random.shuffle(incorrect_indices)

    options = [INCORRECT_ANSWERS[i] for i in incorrect_indices]  # Get one incorrect answer
    correct_option = CORRECT_ANSWERS[correct_index]
    
    # Ensure there are always three options
    if len(options) < 2:
        options.append(INCORRECT_ANSWERS[1 - incorrect_indices[0]])  # Add another incorrect answer if needed

    # Insert the correct answer in a random position among the three
    options.insert(random.randint(0, 2), correct_option)
    
    return options, correct_option

def main():
    continue_practice = True
    
    while continue_practice:
        options, correct_answer = generate_question()
        
        for i, option in enumerate(options):
            print(f"{chr(65+i)}: {option}")
        
        user_guess = input("Which answer is correct? (A, B, C): ")
        if options[ord(user_guess.upper()) - ord('A')] == correct_answer:
            print("Great job!")
        else:
            print("You'll get it next time!")
        
        user_continue = input("Would you like to continue practice? (y/n): ")
        if user_continue.lower() != 'y':
            continue_practice = False

if __name__ == "__main__":
    main()
