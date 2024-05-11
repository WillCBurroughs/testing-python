import sys

# Error checking 
if len(sys.argv) < 2:
    sys.exit("Too Few Arguments")

print("Hello my name is", sys.argv[1])

for arg in sys.argv[1:]:
    print(arg)
