def meow(n: int) -> None:
    """Meow N times"""
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)