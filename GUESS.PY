import random


print("Welcome to the Guessing Game!")
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0:
        print("Please enter a number greater than 0.")
        quit()
else:
    print("Please enter a valid number.")
    quit()
        
r=random.randrange(0,top_of_range)
guesses = 0
while True:
    guesses += 1
    guess =input("make a guess: ")
    if guess.isdigit():
        guess=int (guess)
        if guess == r:
            print("yu got it")
            break
        else:
            if guess < r:
                print("Too low, try again.")
            else:
                print("Too high, try again.") 

    else:
        print("Please enter a valid number.")   

print("You guessed the number in", guess, "tries!")
print("The number was:", r)


