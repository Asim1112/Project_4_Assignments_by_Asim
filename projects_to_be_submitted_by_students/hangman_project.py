import random


words = ["pizza", "burger", "fries"]
word = random.choice(words)
print("Secret word (for testing):", word)


blanks = ["_"] * len(word)
tries = 6
guessed_letters = []


while "_" in blanks and tries > 0:
    print("\nGuess the word:", " ".join(blanks))
    print("Tries left:", tries)

    guess = input("Guess a letter: ").lower()


    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter (a-z)!")
        continue


    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)


    if guess in word:
        print("Good job! The letter is in the word.")
        for i in range(len(word)):
            if word[i] == guess:
                blanks[i] = guess
    else:
        print("Wrong guess!")
        tries -= 1


if "_" not in blanks:
    print("\nYou won! The word was:", word)
else:
    print("\nOut of tries! The word was:", word)
