

def main():
    password_length = 8
    password = get_password(password_length)
    print_password(password)


def get_password(password_length):
    password = input("New Password: ")
    while len(password) < password_length:
        print("Invalid Password Length")
        password = input("New Password: ")
    return password

def print_password(password: str):
    print("Password Set: " + "*" * len(password))

main()

