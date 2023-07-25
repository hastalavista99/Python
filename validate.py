import re

email = input("What's your email? ")
# the 'r' tells python to treat the string as a raw string, ignoring escape characters
if re.search(r"^\w+@\w+\.(edu|gov|com)$", email):
    print("Valid")
else:
    print("Invalid")



