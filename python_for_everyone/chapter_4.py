def main():
    hours_worked = int(input("How many hours have you worked? "))
    pay_rate = int(input("How much do you make per hour? "))
    print(compute_pay(hours_worked, pay_rate))

def compute_pay(hours, pay):
    if hours > 40:
        return hours * pay + (hours - 40) * pay * 0.5
    else:
        return hours * pay

if __name__ == "__main__":
    main()