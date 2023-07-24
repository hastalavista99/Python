# the csv module has a writer() function that allows one to write to csv files
# the writerow() function allows for the writing of headings for those word columns
# the DictWriter()function allows for the writing of dictionaries in the file, does the same job as writer function
import csv


name = input("What's your name? ")
home = input("Where's your home? ")

with open("student.csv", "a") as file:
    writer = csv.writer(file)
    # writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow([name, home])

