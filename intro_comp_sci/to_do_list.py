import json
import os

class ToDoList:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def check_account(self, name):
        return name in self.accounts

    def verify_account(self, name, password):
        if name in self.accounts:
            return self.accounts[name]['password'] == password
        return False

    def create_account(self, name, password):
        if name not in self.accounts:
            self.accounts[name] = {'password': password, 'to_do_items': []}
            self.save_data()
            return "Account created successfully."
        return "Account already exists."

    def add_item(self, name, password, item):
        if self.verify_account(name, password):
            self.accounts[name]['to_do_items'].append(item)
            self.save_data()
            return "Item added successfully."
        return "Incorrect password or account does not exist."

    def read_profile(self, name, password):
        if self.verify_account(name, password):
            return self.accounts[name]['to_do_items']
        return "Incorrect password or account does not exist."

    def save_data(self):
        with open('todolist_data.json', 'w') as file:
            json.dump(self.accounts, file)

    def load_data(self):
        if os.path.exists('todolist_data.json'):
            with open('todolist_data.json', 'r') as file:
                self.accounts = json.load(file)

def main():
    todo = ToDoList()

    # Get information to save for ToDoList
    name = input("What is your username for to list? ")
    password = input("What is the password for this account? ")

    # If there is an account present with this name
    if(todo.check_account(name)):
        while(True):

            # Condition with incorrect verification 
            if(todo.verify_account(name,password) is False):
                password = input("Incorrect Password, what is the password for this account? ")
            # When password is correct, break out of loop
            else:
                break
                    
    # If no account has this name yet? 
    else:
        todo.create_account(name, password)

    # New information to write for ToDoList
    while(True):
        print(todo.read_profile(name, password))
        continue_input = input("Would you like to add new values? y/n ")
        if continue_input == "n":
            break
        else:
            new_items = input("What value would you like to add? ")
            todo.add_item(name, password, new_items)

    print("Thank you for using ToDoList")

if __name__ == "__main__":
    main()

# Have ability to edit items, have ability to delete items, Have user sign-in, store information in database 
# Move functionality to different modules, Add UI for users 