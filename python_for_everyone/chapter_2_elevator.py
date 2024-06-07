def main():
    in_US = True
    are_you_in_us = input("Are you in the US? y/n ")
    if are_you_in_us != "y":
        in_US = False
    what_floor = int(input("What floor are you on? "))
    output = get_floor(what_floor, in_US)
    print(output)

def get_floor(floor, US):
    if US:
        return f"In Europe you would be on floor: {floor - 1}"
    else:
        return f"In the United states you would be on floor: {floor + 1}"

if __name__ == "__main__":
    main()