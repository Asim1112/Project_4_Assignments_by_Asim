MAX_LENGTH: int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print(removed)



def get_lst():
    item = input("Please enter an element of the list or press enter to stop: ")
    my_list = []

    while item != "":
        my_list.append(item)
        item = input("Please enter an element of the list or press enter to stop: ")
    
    return my_list


def main():
    lst = get_lst()
    shorten(lst)


if __name__ == "__main__":
    main()