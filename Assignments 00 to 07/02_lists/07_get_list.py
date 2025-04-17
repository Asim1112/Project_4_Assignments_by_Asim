def main():
    my_list = []
    value = input("Enter a value: ")
    
    while value != "":
        my_list.append(value)
        value = input("Enter a value: ")

    print(my_list)



if __name__ == "__main__":
    main()
        