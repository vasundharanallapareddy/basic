import random
import time

def intro():
    global name  # Make name accessible in pick function
    print("May I ask you for your name?")
    name = input()  # Ask for the name
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick(number):
    guesses_taken = 0
    while guesses_taken < 6:  # If the number of guesses is less than 6
        time.sleep(0.25)
        enter = input("Guess: ")  # Prompt to enter guess
        try:
            guess = int(enter)  # Store the guess as an integer instead of a string    

            if 1 <= guess <= 200:  # If the guess is in range
                guesses_taken += 1  # Increment guess count
                if guesses_taken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(0.5)
                        print("Try Again!")
                if guess == number:
                    break  # Correct guess
            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")

        except ValueError:  # If a non-number was entered
            print(f"I don't think that {enter} is a number. Sorry")
            
    if guess == number:
        print(f'Good job, {name}! You guessed my number in {guesses_taken} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {number}')

playagain = "yes"
while playagain.lower() in ["yes", "y"]:
    number = random.randint(1, 200)  # Pick the number between 1 and 200
    intro()
    pick(number)
    print("Do you want to play again?")
    playagain = input()
