import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("user_info.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])