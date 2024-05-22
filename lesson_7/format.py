import re

name = input("What's your name? ").strip()

# Adding walrus operator (:=) to assign value and ask boolean question 
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
