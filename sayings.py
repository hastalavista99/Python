def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


# the __name__ variable is a special python variable whose value is automatically set by python to be "__main__" when running programs from the command line
# the main function will not be called when the file is imported
if __name__ == "__main__":
    main()
