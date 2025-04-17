from hashlib import sha256


def hash_password(password):
    return sha256(password.encode()).hexdigest()



stored_logins = {
    "asim@example.com": hash_password("AsimStrongPass123"),
    "ali@example.com": hash_password("AliSecure456")
}



def login(email, stored_logins, password_to_check):
    if stored_logins[email] == hash_password(password_to_check):
        return True
    return False


print(login("asim@example.com", stored_logins, "AsimStrongPass123"))
print(login("asim@example.com", stored_logins, "WrongPass"))



def main():
    print(login("asim@example.com", stored_logins, "AsimStrongPass123"))
    print(login("asim@example.com", stored_logins, "WrongPass"))



if __name__ == "__main__":
    main()