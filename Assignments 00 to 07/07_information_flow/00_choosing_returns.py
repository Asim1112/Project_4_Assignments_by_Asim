AGE : int = 18

def is_adult(age: int):
    if age >= AGE:
        return True
    
    return False
    

def main():
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    



if __name__ == "__main__":
    main()