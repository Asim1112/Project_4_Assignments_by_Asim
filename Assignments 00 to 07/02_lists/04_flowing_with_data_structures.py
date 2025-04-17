def add_three_copies(lst, msg):
    lst.append(msg)
    lst.append(msg)
    lst.append(msg)


def main():
    Message = input("Enter a message to copy: ")
    List = []
    
    print("List before",List)   
    
    add_three_copies(List, Message)

    print("List after", List)


if __name__ == "__main__":
    main()

    