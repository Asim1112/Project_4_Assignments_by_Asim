
def get_first_element(lst):
    print(lst[0])





def main():
    my_list = []
    item = input("Enter an item (press Enter to stop): ")

    while item != "":
        my_list.append(item)
        item = input("Enter an item (press Enter to stop): ")


    get_first_element(my_list)


if __name__ == "__main__":
    main()

