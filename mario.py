"""

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()
"""

# Printing a 3 * 3 grid

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main()
