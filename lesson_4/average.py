import sys

# Error checking 
if len(sys.argv) < 2:
    sys.exit("Too Few Arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many argumenets")

print("Hello my name is", sys.argv[1])
