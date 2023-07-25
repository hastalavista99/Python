import re

email = input("What's your email? ")

if re.search(r".+@.+\.com", email):
    print("Valid")
else:
    print("Invalid")



