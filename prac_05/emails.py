"""
CP1404/CP5632 Practical
Email Recording
Estimate 15mins
Took 10mins
"""

def main():
 email = input("Enter Your Email: ")
 name = get_name_from_email(email)
 email_names = {}
 while email != "":
    email_names[email] = name
    print(email_names)
    email = input("Enter Your Email: ")
    name = get_name_from_email(email)
 for email,name in email_names.items():
     print(f"{name}, {email}")



def get_name_from_email(email):
    while email != "":
     """Split the name from the email and check if it's correct """
     email_parts = email.split("@")
     check = input(f"Is {email_parts[0]}  your name? (T/F)")
     if check == "T":
        name = email_parts[0]
     else:
        name = input("Please Enter Name: ")
     return name
    else:
        return ""

main()
