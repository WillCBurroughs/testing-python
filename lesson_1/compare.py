def main():
    age = int(input("How old are you? "))
    bouncer(age)

def bouncer(age):
    if age == 21:
        print("drinks on me!")
    elif age > 21:
        print("You're good to go")
    else:
        print("You are too young to get in")

main()