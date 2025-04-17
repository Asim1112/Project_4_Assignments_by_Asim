import random

NUMBER_SIDES: int = 6



def main():
    die1: int = random.randint(1, NUMBER_SIDES)
    die2: int = random.randint(1, NUMBER_SIDES)
    total: int = die1 + die2

    
    print("Dice have", NUMBER_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

    

if __name__ == "__main__":
    main()