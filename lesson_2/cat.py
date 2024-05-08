def main():
    print_numbers()

# Step 1 for simple loop python 
for i in [0,1,2]:
    print("meow")

# Alternative for simple loop 
for i in range(5):
    print(i)

# Not utilizing value 
for _ in range(3):
    print("Hello")

# Multiplying values of string 
print("Multiple \n" * 3, end="")

# Forcing input greater than 0 
def print_numbers():
    while True:
        n = int(input("What value is n? "))

        if n > 0:
            break

    for i in range(n):
        print(i)

main()