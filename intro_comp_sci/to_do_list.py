import json
import os
from tkinter import *
from tkinter import ttk


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
    
    # Edit information at the given index
    def edit_information(self, name, password, index, new_info):
        if self.verify_account(name, password):
            if 0 <= index < len(self.accounts[name]['to_do_items']):
                self.accounts[name]['to_do_items'][index] = new_info
                self.save_data()
                return "Item edited successfully."
            else:
                return "Invalid index."
        return "Incorrect password or account does not exist."

    def delete_item(self, name, password, index):
        if self.verify_account(name, password):
            if 0 <= index < len(self.accounts[name]['to_do_items']):
                del self.accounts[name]['to_do_items'][index] 
                self.save_data()
                return "Item edited successfully."
            else:
                return "Invalid index."
        return "Incorrect password or account does not exist."

# changing name of root 
def complete_sign_in():
    root.title("To Do App")

def main():

    global save_name, save_password, root

    # Allows for main call to Tkinter 
    root = Tk()

    # Creates new frame for Tkinter 
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    root.title("Sign In")

    # Input labels
    ttk.Label(frm, text="Username: ").grid(column=0, row=0)

    # Input for name 
    save_name = ttk.Entry(frm).grid(column=1, row=0)

    # Main label of grid 
    ttk.Label(frm, text="Password: ").grid(column=0, row=1)

    # Input for name 
    save_name = ttk.Entry(frm).grid(column=1, row=1)

    # Used to close program
    ttk.Button(frm, text="Login", command=complete_sign_in).grid(column=1, row=2)

    # Used to run program
    root.mainloop()

    # Used to call main ToDoList function
    todo = ToDoList()

    # Get information to save for ToDoList
    name = input("What is your username for to list? ")
    password = input("What is the password for this account? ")

    # If there is an account present with this name
    if(todo.check_account(name)):
        while(True):

            # Condition with incorrect verification 
            if(todo.verify_account(name, password) is False):
                password = input("Incorrect Password, what is the password for this account? ")
            # When password is correct, break out of loop
            else:
                break
                    
    # If no account has this name yet? 
    else:
        todo.create_account(name, password)

    # New information to write for ToDoList
    while(True):
        items = todo.read_profile(name, password)
        print(items)
        action = input("What would you like to do? (add/edit/delete/quit) ").lower()
        if action == "quit":
            break
        elif action == "add":
            new_items = input("What value would you like to add? ")
            todo.add_item(name, password, new_items)
        elif action == "edit":
            try:
                index = int(input("Enter the index of the item you want to edit: "))
                new_info = input("Enter the new information: ")
                result = todo.edit_information(name, password, index, new_info)
                print(result)
            except ValueError:
                print("Please enter a valid number for the index.")
        elif action == "delete":
            try:
                index = int(input("Enter the index of the item you want to delete: "))
                result = todo.delete_item(name, password, index)
                print(result)
            except ValueError:
                print("Please enter a valid number for the index.")
        else:
            print("Invalid action. Please choose 'add', 'edit', 'delete', or 'quit'.")

    print("Thank you for using ToDoList")

if __name__ == "__main__":
    main()

# Need to add UI with functions, Have ability to edit items, have ability to delete items, Have user sign-in, store information in database 
# Move functionality to different modules, Add UI for users 