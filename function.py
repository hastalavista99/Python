# Introduction to functions in python
# the function argument can be given a default value
# def hello(to="world"):
#     print("hello,", to)


# hello()
# name = input("What is your name: ")
# hello(name)

# Return Keyword

def main():
    a = int(input("Enter a number: "))
    print("a squared is", square(a))

def square(n):
    return n*n # or pow(n, 2) also does the trick


if  __name__ == "__main__":
    main()
