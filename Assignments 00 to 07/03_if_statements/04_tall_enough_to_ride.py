HEIGHT : int = 50

def main():
    length = float(input("How tall are you? "))
    if length >= HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


if __name__ == '__main__':
    main()