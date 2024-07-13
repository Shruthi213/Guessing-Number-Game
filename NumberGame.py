import random

top_range = input("Enter random number: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Enter number larger than 0:  ")
    quit()
else:
    print("Type a number next time")
    quit()

random_number = random.randint(0, top_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time")
        continue
    if user_guess == random_number:
        print("you got it: ")
        break
    else:
        if user_guess > random_number:
            print("Yor are above the number: ")
        else:
            print("You are below the number: ")


print("you got it in", guesses, "guesses")



