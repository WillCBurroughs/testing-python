def main():
   x = get_int()
   print(f"x is {x}")


# will keep asking user for value until acceptable value
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("X is not an integer")

main()