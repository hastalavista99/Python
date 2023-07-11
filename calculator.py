# this program contains int functions and methods
# INT
# python takes keyboard input as strings even if number values are keyed in
# int()function converts the input from str ito int
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))


# print(a + b)

# the lines above can be summarized as below
# print(int(input("Enter first number: ")) + int(input("Enter second number: ")))

# FLOAT
# float function allows processing of decimal numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# round(number[, ndigits]), this rounds up decimal to the nearest integer, ndigits specifies number of decimal places
c = round(a + b)

# print(f"{c:,}") this puts a comma after every third digit
print(f"{c:.2f}") # this specifies that the output should be to 2 decimal places
