import random



print("Welcome to the 'Guess your Number' Game!")
print("Think of a number between 1 and 99")
input("Press enter when you are ready...")


high: int = 99
low: int = 1
feedback = ""


while feedback != "c":
    guess = random.randint(low, high)
    print(f"My guess is: {guess}")

    
    feedback = input("is it (H)igh, (L)ow or (C)orrect? ").lower()


    if feedback == "h":
        high  = guess - 1
    elif feedback == "l":
        low = guess + 1
    elif feedback == "c":
        print(f" Yay! I guessed your number {guess} correctly!")
    else:
        print("Please enter only 'L', 'H' or 'C' ")





