# Unpacking

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]
# unpack a list by using an asterisk and two asterisks to unpack a dictionary
# unpacking passes the items in the list into the respective arguments for the total function
# print(total(*coins), "Knuts")

def f(*args, **kwargs):
    print("named:", kwargs)

f(galleons=100, sickels=50, knuts=25)

