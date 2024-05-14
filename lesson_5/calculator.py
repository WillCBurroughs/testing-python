
def main():
    x = int(input("What's x? "))
    print("x square is", square(x))

def square(val):
    return val * val

if __name__ == "__main__":
    main()