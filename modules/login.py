import re
from modules.project import project_Menue

def email_check():
    email = input("Please Enter Your Login Email: ")
    valid_email = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
    is_match = bool(valid_email)
    if is_match == True:
        return email
    else:
        print("Please Enter A Valid E-mail")
        return email_check()

def password_check():
    password = input("Please Enter Your Password: ")
    if len(password) == 0:
        print("Please Enter A Valid Password")
        password_check()
    else:
        return password


def valid_data():
    email =  email_check()
    password = password_check()
    with open("modules/users.txt") as file:
        if email and password in file.read():
            project_Menue()
        else:
            print("Your Login Info Was Not Found")

