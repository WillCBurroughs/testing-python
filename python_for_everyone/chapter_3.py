def main():
    hold_user_name = input("What is your name? ")
    hold_user_password = input("What is your password? ")

    find_users(hold_user_name, hold_user_password)

# Empty dictionary used to hold users
hold_users = {}

# Used to create new instance in hold_users
def save_user(name, password):
    hold_users[name] = password
    print(f"Saved new user {name}")

def recover_user(name, password):
    print(f"Found user {name} within users")

def find_users(name, password):
    if name in hold_users:
        if hold_users[name] == password:
            recover_user(name, password)
        else:
            print(f"Password for user {name} is incorrect")
    else:
        save_user(name, password)

if __name__ == "__main__":
    main()