
# will keep asking user for value until acceptable value
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("X is not an integer")
    else:
        break

print(f"x is {x}")