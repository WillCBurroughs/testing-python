def main():
   x = get_int("What is value to pass? ")
   print(f"x is {x}")


# will keep asking user for value until acceptable value
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()