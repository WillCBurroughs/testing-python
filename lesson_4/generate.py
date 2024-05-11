from random import choice

def main():
    repeat_times = int(input("How many times to flip? "))
    get_percentages(repeat_times)

# Simple program to randomly flip coin
def flip_coin():
    return choice(["Heads","Tails"])

# Flip the coin given numbers of times and get true percentages 
def get_percentages(times_to_repeat):
    times_option_1 = 0
    times_option_2 = 0 

    if(times_to_repeat <= 0):
        return 0

    for _ in range(times_to_repeat):
        hold_flip = flip_coin()
        if hold_flip == "Heads":
            times_option_1 += 1
        elif hold_flip == "Tails":
            times_option_2 += 1

    percentage_heads = 100 * (times_option_1 / times_to_repeat)
    percentage_tails = 100 * (times_option_2 / times_to_repeat)
    
    print(f"Percent Heads: {percentage_heads}%")
    print(f"Percent Tails: {percentage_tails}%")

main()