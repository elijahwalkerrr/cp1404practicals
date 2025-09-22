

def main():
    get_password()


def get_password():
    password = input("New Password: ")
    while len(password) < 8:
        print("Invalid Password Length")
        password = input("New Password: ")
    print_password(password)


def print_password(password: str):
    print("Password Set: " + "*" * len(password))


main()

