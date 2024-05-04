def main():
    test_input = input("What is the secret to live and happiness? ")
    treat_output(is_input_42(test_input))

def is_input_42(passed_value):
    return passed_value == "42" or passed_value == "Forty Two" or passed_value == "forty-two"

def treat_output(truth_value):
    if(truth_value):
        print("Yes")
    else:
        print("No")


main()