def meow(n: int) -> None:
    """
    Docu-String
    Meow N times
    :param n: Number of times to meow
    :type n: int
    """
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)