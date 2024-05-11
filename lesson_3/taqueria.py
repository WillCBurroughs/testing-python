def main():
    get_order_price()


def get_order_price():
    total_price = 0.00 

    order_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    while True:
        get_request = input("Item: ")
        try:
            next_value = order_menu[get_request]
            total_price += next_value
            print(f"Total {total_price}")
        except:
            pass

main()
