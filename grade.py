
# The 'and ' keyword is used when using more than one condition, granted both conditions should be true in order to run the statement under it
score = int(input("Enter score: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <= 89:
    print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
else:
    print("Grade F")

# the program above can be simplified as follows:


score = int(input("Enter score: "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")


