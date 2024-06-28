import re

def main():
    x = "From Stephen, you can reach me at stephen@example.com. How are you doing great to see you - 3:30 Wednesday"
    y = re.findall(r'\S+@\S+', x)
    print(y)

if __name__ == "__main__":
    main()