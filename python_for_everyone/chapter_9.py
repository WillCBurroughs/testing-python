def main():
    counts = dict()

    names = ["will", 'jon', 'gadi', 'ryan', 'peyton', 'josh', 'josh']

    for name in names:
        counts[name] = counts.get(name, 0) + 1

    print(counts)

if __name__ == "__main__":
    main()