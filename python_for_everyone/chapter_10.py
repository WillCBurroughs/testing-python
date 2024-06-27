def main():
    # Tuples are immutable
    simple_tuple = ('hello', 'hey', 'oye')
    print(simple_tuple)
    print(dir(simple_tuple))

    # left sided tuples 
    (hello, ayy) = ("hello", "ayy")
    print(hello)

if __name__ == "__main__":
    main()