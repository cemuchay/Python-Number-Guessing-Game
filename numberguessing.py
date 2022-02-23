import random
import math

lower = int(input("\nPlease enter lower bound: "))
upper = int(input("\nPlease enter upper bound: "))

x = random.randint(lower, upper)

print("\nYou have a maximum of ", round(math.log(upper - lower + 1, 2)), "number of guesses")

count = 0
 
while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input('Please Guess a Number: '))

    if guess == x:
        print('\nCongratulations You did it After', count, "Attempt(s)" )
        break

    elif guess < x:
        print("\nYou guessed too low, Perhaps a Higher Number?","You have ", round(math.log(upper - lower + 1, 2)) - count, "Number of guesses Remaining")

    elif guess > x:
        print("\nYou guessed too high, Perhaps a lower Number?", "You have ", round(math.log(upper - lower + 1, 2)) - count, "Number of guesses Remaining")

while count > round(math.log(upper - lower + 1, 2)):
    print("\nYour Chances are up, The correct Number Is", x)
