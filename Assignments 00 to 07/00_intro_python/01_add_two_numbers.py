def main():
  user_first_input: str = input("Please enter the first number: ")
  converting_first: int = int(user_first_input)
  user_second_input: str = input("Please enter the second numebr: ")
  converting_second: int = int(user_second_input)

  result: int = converting_first + converting_second
  print("The sum of the both numbers is:", result)



if __name__ == '__main__':
  main()