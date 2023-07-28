import re

email = input("What's your email? ").strip()
# the 'r' tells python to treat the string as a raw string, ignoring escape characters
if re.search(r"^\w+(\.\w+)?(\.\w+)?@(\w\.)?\w+\.(edu|gov|com)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



