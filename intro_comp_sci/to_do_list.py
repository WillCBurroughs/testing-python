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
                return "Item deleted successfully."
            else:
                return "Invalid index."
        return "Incorrect password or account does not exist."

# Need to test and load in users
def validate_user():
    print("Validated")

    name = save_name.get()
    password = save_password.get()

    # If there is an account present with this name
    if todo.check_account(name):
        if not todo.verify_account(name, password):
            incorrect_password()
        else:
            switch_to_main(name, password)
    else:
        todo.create_account(name, password)
        switch_to_main(name, password)

# Used to flash incorrect password
def incorrect_password():
    incorrect_password_label = ttk.Label(frm, text="Incorrect Password, try again or create new account")
    incorrect_password_label.grid(column=1, row=3)

def add_list_item(name, password):
    new_item = new_item_entry.get()
    if new_item:
        todo.add_item(name, password, new_item)
        # Clear the entry field
        new_item_entry.delete(0, END)
        # Refresh the list display
        update_list_display(name, password)

def update_list_display(name, password):
    # Clear existing items
    for widget in new_home.winfo_children():
        widget.destroy()

    ttk.Label(new_home, text="Here are your list items: ").grid(column=0, row=0)

    items = todo.read_profile(name, password)

    idx = 0
    for idx, item in enumerate(items, start=1):
        ttk.Label(new_home, text=f"{idx}. {item}").grid(column=0, row=idx)

    new_item_entry.grid(column=0, row=idx + 1)
    add_item_button.grid(column=1, row=idx + 1)

def switch_to_main(name, password):
    # Need to change name of root 
    root.title("To Do App")

    # Need to remove frame and add new frame 
    for widget in root.winfo_children():
        widget.destroy()

    # Need to add new frame and load in called in values
    global new_home, new_item_entry, add_item_button
    new_home = ttk.Frame(root, padding=10)
    new_home.grid()

    new_item_entry = ttk.Entry(new_home)
    add_item_button = ttk.Button(new_home, text="Add a list item", command=lambda: add_list_item(name, password))

    update_list_display(name, password)

# changing name of root 
def complete_sign_in():
    # Need to validate user sign in, then switch to main
    validate_user()

def main():
    global save_name, save_password, root, frm, new_home, ttk, todo

    # Allows for main call to Tkinter 
    root = Tk()

    # Creates new frame for Tkinter 
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    root.title("Sign In")

    # Input labels
    ttk.Label(frm, text="Username: ").grid(column=0, row=0)

    # Input for name 
    save_name = ttk.Entry(frm)
    save_name.grid(column=1, row=0)

    # Main label of grid 
    ttk.Label(frm, text="Password: ").grid(column=0, row=1)

    # Input for password 
    save_password = ttk.Entry(frm, show='*')
    save_password.grid(column=1, row=1)

    # Used to close program
    ttk.Button(frm, text="Login", command=complete_sign_in).grid(column=1, row=2)

    # Used to call main ToDoList function
    todo = ToDoList()

    # Used to run program
    root.mainloop()

if __name__ == "__main__":
    main()
    
# Need to add UI with functions, Have ability to edit items, have ability to delete items, Have user sign-in, store information in database 
# Move functionality to different modules, Add UI for users 

# Need to load in list items. Need to add create section account, Need to cleanup code base, Need to save values in DB 
# Need to deploy project 