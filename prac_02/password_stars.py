

def main():
    password = get_password()
    print_password(password)


def get_password():
    password = input("New Password: ")
    while len(password) < 8:
        print("Invalid Password Length")
        password = input("New Password: ")
    return password

def print_password(password: str):
    print("Password Set: " + "*" * len(password))

main()

