POSITIVE : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + POSITIVE)

    user_feedback = input()
    while user_feedback != POSITIVE:
        print("That was not the affirmation.")

        print("Please type the following affirmation: " + POSITIVE)
        user_feedback = input()

    print("That's right! :)")



if __name__ == '__main__':
    main()