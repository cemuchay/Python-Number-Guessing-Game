import random
import math

def check_plural(input_num):
    if input_num > 0:
        return 's'
    else:
        return ''

# Collecting Integer Inputs
lower = int(input("\nPlease enter lower bound: "))
upper = int(input("\nPlease enter upper bound: "))

# Generating pseudo random Int between bounds
num = random.randint(lower, upper)

guesses = round(math.log(upper - lower + 1, 2))

print("\nYou have a maximum of", guesses, "number of guess" + check_plural(guesses))

# Initializing Count
count = 0
 
while count < guesses:
    count += 1

    # Matching Guess to Random number
    guess = int(input('Please Guess a Number: '))
    
    attemptsLeft = guesses - count
    
    if count == guesses:
        print(f"\nYour chances are up. The correct number is {num}.")
        break
    
    if guess == num:
        print(f'\nCongratulations! You did it after {count} attempt{check_plural(count)}. {attemptsLeft} attempt{check_plural(attemptsLeft)} remaining.')
        break

    elif guess < num:
        print(f"\nYou guessed too low. Perhaps a higher number? You have {attemptsLeft} attempt{check_plural(attemptsLeft)} remaining.")

    elif guess > num:
        print(f"\nYou guessed too high. Perhaps a lower number? You have {attemptsLeft} attempt{check_plural(attemptsLeft)} remaining.")

   
