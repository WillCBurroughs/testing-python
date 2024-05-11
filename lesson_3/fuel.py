def main():
    output = get_fraction()
    print(f"gas remaining is {output}")

def get_fraction():
    while True:
        value_returned = input("What fraction of gas remains? ").strip()
        hold_values = []
        try:
            hold_values = value_returned.split("/")
            hold_first_value = int(hold_values[0])
            hold_second_value = int(hold_values[1])
            if hold_first_value == 0 and hold_second_value != 0:
                return "E"
            returnvalue = (hold_first_value / hold_second_value)
            if returnvalue < 0.01:
                return "E"
            elif returnvalue > 0.99:
                return "F"
            else:
                return str((100 * (hold_first_value / hold_second_value))) + "%"
        except (ValueError, ZeroDivisionError):
            pass

main()