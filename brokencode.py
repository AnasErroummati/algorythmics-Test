# Exercise:
# Ask the user to enter a number.
# - If the number is positive, print "Positive".
# - If the number is negative, print "Negative".
# - If the user enters 0, the program should stop immediately.
# Use a loop to continuously prompt for input until 0 is entered.
while True:
    number = int(input("Enter a number:(Enter 0 to stop):"))
    if number == 0:
        print("Stopingthe program!")
        break
    elif number > 0:
        print("Postive!")
    else:
        print("Negative!")

