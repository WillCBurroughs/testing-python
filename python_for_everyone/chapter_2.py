# Can not use reserved word as variable names 
# variable names must start with letter or underscore 

# can have letters and numbers and underscores 
# bad practice to use same words for variables only differentiating based on case 

# Expressions are composed of operators 
# We are limited by our keyboards 

# operator precedence is important PEMDAS followed. Remainder equivalent to multiplication and division 
# combining types that are incompatible and can't be cast will throw errors 

# can call type to test type 

def main():
    user_input = input("What to send in? ")
    print(get_type(user_input))

def get_type(value):
    return type(value)

if __name__ == "__main__":
    main()