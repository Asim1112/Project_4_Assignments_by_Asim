INCHES_IN_FOOT: int = 12

def main():
    number_of_feet: float = float(input("Enter number of feet: "))
    feet_in_inches: float = number_of_feet * INCHES_IN_FOOT

    print("This is", feet_in_inches, "inches!")


if __name__ == "__main__":
    main()