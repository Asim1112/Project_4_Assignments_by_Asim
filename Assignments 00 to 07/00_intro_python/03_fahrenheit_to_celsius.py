def main():
    fahrenheit = input("Enter the temperature in Fahrenheit: ")
    fahrenheit_to_decimal = float(fahrenheit)

    celsius = (fahrenheit_to_decimal - 32) * 5.0 / 9.0
    print(f"Temperature: {fahrenheit_to_decimal}F = {celsius}C")



if __name__ == '__main__':
    main()
