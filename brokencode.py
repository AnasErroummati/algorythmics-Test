# Exercise:
# Ask the user to enter a number.
# - If the number is positive, print "Positive".
# - If the number is negative, print "Negative".
# - If the user enters 0, the program should stop immediately.
# Use a loop to continuously prompt for input until 0 is entered.
while True:
    nn = int(input('entreu un nombre'))
    if nn == 0:
        print('ffg')
        break
    elif nn > 0:
        print('posi')
    else:
        print('negatives')
        print('nn')