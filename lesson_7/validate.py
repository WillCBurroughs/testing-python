
import re

email = input("What's your email? ").strip()

# Alternative for [a-zA-Z0-9_] is simply \w which is shortcut for a word 
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# This lesson does a great job of showing why we should use Regex Libraries for validation rather than making the expression ourselves
