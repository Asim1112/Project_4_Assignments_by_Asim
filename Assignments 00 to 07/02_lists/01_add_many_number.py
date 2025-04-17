def adding_numbers(numbers) -> int:
    """
    Takes in a list of numbers and return the sum of those numbers.
    """

    total_numbers: int = 0
    for number in numbers:
        total_numbers += number

    return total_numbers



def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    sum_of_numbers: int = adding_numbers(numbers)
    print(sum_of_numbers)



if __name__ == "__main__":
    main()