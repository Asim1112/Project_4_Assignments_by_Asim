import random


print("Welcome to guess the number game!")

guess: int = 0
secret_number: int = random.randint(1 , 99)
tried: int = 0


while guess != secret_number:
    guess = int(input("Enter the number between 1 and 99: "))
    tried += 1
    
    
    if guess > secret_number:
        print("It's Too High! Try again.")
    elif guess < secret_number:
        print("It's Too Low! Try again.")
    else:
        print("Congratulations! You guessed it right in " + str(tried) + " times")

