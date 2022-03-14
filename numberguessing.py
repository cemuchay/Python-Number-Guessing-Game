import random
import math

# Collecting Integer Inputs
lower = int(input("\nPlease enter lower bound: "))
upper = int(input("\nPlease enter upper bound: "))

# Generating pseudo random Int between bounds
x = random.randint(lower, upper)

print("\nYou have a maximum of ", round(math.log(upper - lower + 1, 2)), "number of guesses")

# Initializing Count
count = 0
 
 
while count < round(math.log(upper - lower + 1, 2)):
    count += 1

    # Matching Guesss to Random number
    guess = int(input('Please Guess a Number: '))

    if guess == x:
        print('\nCongratulations You did it After', count, "Attempt(s)" , "\n and", round(math.log(upper - lower + 1, 2)) - count, "Guess(es) remaining")
        break

    elif guess < x:
        print("\nYou guessed too low, Perhaps a Higher Number?","You have ", round(math.log(upper - lower + 1, 2)) - count, "Number of guess(es) Remaining")

    elif guess > x:
        print("\nYou guessed too high, Perhaps a lower Number?", "You have ", round(math.log(upper - lower + 1, 2)) - count, "Number of guess(es) Remaining")

    if count == round(math.log(upper - lower + 1, 2)):
      print("\nYour Chances are up, The correct Number Is", x )
