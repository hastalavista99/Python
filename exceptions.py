# exceptions are errors or bugs in your code
# the except statement catches exceptions, one can specify the exceptions to be caught
# the else statement executes if the exception is not caught

while True:
    try:
        x = int(input("What's x? "))

    except ValueError:
        print("x is not an integer")
    else:
        break


print(f"x is {x}")



