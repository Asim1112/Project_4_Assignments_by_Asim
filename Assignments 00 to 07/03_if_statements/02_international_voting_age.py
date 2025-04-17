PETURKSBOUIPO_VOTING_AGE: int = 16
STANLAU_VOTING_AGE: int = 25
MAYENGUA_VOTING_AGE: int = 48


def main():
    user_age = int(input("How old are you: "))

    if user_age >= PETURKSBOUIPO_VOTING_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_VOTING_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_VOTING_AGE) + ".")


    
    if user_age >= STANLAU_VOTING_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_VOTING_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_VOTING_AGE) + ".")



    if user_age >= MAYENGUA_VOTING_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_VOTING_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_VOTING_AGE) + ".")


if __name__ == "__main__":
    main()