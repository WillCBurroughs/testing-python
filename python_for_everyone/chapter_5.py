def main():

    user_sum = 0 
    user_total = 0
    user_average = 0 

    test_input = ""

    while test_input != "done":
        test_input = input("What value would you like to add? ")

        if test_input == "done":
            user_average = user_sum / user_total
            print(user_sum, user_total, user_average)
            break

        try:
            test_input = int(test_input)
        except:
            print("Must give a number")
            continue
            

        user_sum += test_input
        user_total += 1



if __name__ == "__main__":
    main()