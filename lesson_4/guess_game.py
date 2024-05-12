import random

def main():
    test_input()

def generate_level(level):
    return random.randint(1, level)

def get_input():
    value_return = int(input("What guess would you like? "))
    return value_return

def test_input():

    number_to_approach = int(input("What Range would you like? "))
    number = generate_level(number_to_approach)

    time_to_break = False
    while not time_to_break:
        guess = get_input()

        if number > guess:
            print("Too small!")
        elif number < guess:
            print("Too large!")
        elif number == guess:
            print("Just right!")
            time_to_break = True

main()