import random
import os

#Function for clearing console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# This function explains rules and asks for name of p  layer.
def intro():
    print("Welcome to the Random number guessing game!")
    print("May I ask your name?")
    name = input()
    clearConsole()
    print(f"Hello {name}! Let me explain rules to you quickly.")
    print("I have picked number between 1-10. You get 3 guesses to get it right.")
    print("With every wrong answer you will lose a live. If you guess right you win the game!")
    print("Let's get started!")

#This function is for gameplay. It lets player guess and tell if they win or lose
def gameplay():
    #Defining starting points for variables in code
    computer_choice = random.randint(1, 10)
    player_lives = 3
    end_of_game = False
    player_guesses = []

    while not end_of_game:
        if player_lives > 0:
            guess = int(input("Guess the number! "))
            if guess in player_guesses:
                print(f"You already guessed {guess}. Try again!")
            elif guess == computer_choice:
                print(f"You won game with {player_lives} live(s) remaining.")
                end_of_game = True
            elif guess > computer_choice:
                player_lives -= 1
                player_guesses.append(guess)
                print(f"{guess} is too high! You have {player_lives} live(s) remaining.")
            else:
                player_lives -= 1
                player_guesses.append(guess)
                print(f"{guess} is too low. You have {player_lives} live(s) remaining.")
        else:
            end_of_game = True
            print("You lost!")




while True:
    intro()
    gameplay()
    print("Do you want play again? Yes/no ")
    again = input()
    if again.lower() not in ("y", "yes"):
        print("Thank you for playing! See you next time!")
        break
    else:
        clearConsole()
        continue