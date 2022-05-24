import random
print("Number Guessing Game")
randomNumber = random.randint(1, 9)
print("Guess a number from 1-9")
chances = 0
while chances < 5:
    guess=int(input("Enter your guess! "))
    if guess == randomNumber:
        print("Congradulations, You Win!")
        break
    elif guess < randomNumber:
        print("Your guess was too low, guess a higher number")
    else:
        print('Your guess was too high, guess a lower number')
    chances += 1
if not chances < 5:
    print("You Lose.")