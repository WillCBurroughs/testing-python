
def main():
    print(count_lines())

def count_lines():

    total_lines = 0

    with open("lines.txt", "r") as file:
        for line in file:
            hold_line = line
            hold_line = hold_line.strip()
            if hold_line == "" or hold_line == "\n" or hold_line.startswith("#"):
                continue
            else:
                total_lines += 1

    return total_lines


if __name__ == "__main__":
    main()

