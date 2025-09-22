password = input("New Password: ")

def main():
    while len(password) < 8:
        print ("Invalid Password Length")
        password = input("New Password: ")
    print ("Password Set: " + "*" * len(password))

main()