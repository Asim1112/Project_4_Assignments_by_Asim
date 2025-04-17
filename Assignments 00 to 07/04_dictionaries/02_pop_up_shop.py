def main():
    fruit_prices: dict = {
        "apple": 10,
        "durian": 25,
        "jackfruit": 30,
        "kiwi": 12.5,
        "rambutan": 7,
        "mango": 5
    }

    total: float = 0.0

    for fruit in fruit_prices:
        quantity = input("How many " + fruit + " you want to buy: ")
        total = total + int(quantity) * fruit_prices[fruit]

    print(f"Your total is {total}")

    
if __name__ == '__main__':
    main()