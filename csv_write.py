# the csv module has a writer() function that allows one to write to csv files
# the writerow() function allows for the writing of headings for those word columns
import csv


name = input("What's your name? ")
home = input("Where's your home? ")

with open("student.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
