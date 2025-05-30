def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():

    lst = [10, 20, 30, 40, 50]
    print("Current list:", lst)
    
   
    print("\nChoose an operation: access, modify, slice")
    operation = input("Enter operation: ").lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        result = access_element(lst, index)
        print("Result:", result)

    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")

        if new_value.isdigit():
            new_value = int(new_value)
        result = modify_element(lst, index, new_value)
        print("Updated list:", result)

    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        result = slice_list(lst, start, end)
        print("Sliced list:", result)

    else:
        print("Invalid operation.")


index_game()
