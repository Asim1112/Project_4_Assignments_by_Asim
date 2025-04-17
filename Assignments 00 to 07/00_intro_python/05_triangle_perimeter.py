def main():
    side1: int = int(input("What is the length of side 1? "))
    side2: int = int(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))
    
    sum_of_lengths: float = float(side1 + side2 + side3)
    print(f"The perimeter of the triangle is {sum_of_lengths}")


if __name__ == "__main__":
    main()