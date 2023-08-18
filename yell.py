# this program will return uppercase words list
def main():
    yell("This", "is", "CS50")


def yell(*words):
    # use list conprehension
    uppercased = [word.upper() for word in words]
    # or use map
    # uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()
