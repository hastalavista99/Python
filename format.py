# the program below takes a comma separated name (last_name, first_name) and outputs it in the more common order(first_name last_name)

import re

name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"hello, {name}")

matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")

