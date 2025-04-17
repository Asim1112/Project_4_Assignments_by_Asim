def get_user_numbers():
    user_input = input("Enter a number (or press Enter to stop): ")
    my_list = []

    while user_input != "":
        number = int(user_input)     # Convert only if not empty
        my_list.append(number)
        user_input = input("Enter a number (or press Enter to stop): ")

    return my_list



def count_nums(num_1st):
    my_dict = {}
    for num in num_1st:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] += 1
    
    return my_dict




def print_counts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")




def main():
    user_numbers = get_user_numbers()
    count_numbers = count_nums(user_numbers)
    print_counts(count_numbers)




if __name__ == "__main__":
    main()


