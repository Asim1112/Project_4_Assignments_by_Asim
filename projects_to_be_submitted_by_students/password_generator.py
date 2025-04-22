import random

print("Welcome to Password Generator")


characters  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*().,?0987654321"

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Enter the length of your password: ")
length = int(length)


print("\nYour passwords are here")


for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(characters)

    print(passwords)
