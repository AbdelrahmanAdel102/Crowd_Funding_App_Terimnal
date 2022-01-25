import re
class USER:
    def __init__(self, f_name, l_name, email, password, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password
        self.phone = phone

    def write_to_file (self):
        get_data = open("users.txt", 'r').read()
        file = open("users.txt", 'a+')
        if len(get_data) > 0:
            file.write(" First_Name: {0} | Last_Name: {1} | E-mail: {2} | Password: {3} | Phone: {4} ".format(self.f_name, self.l_name, self.email,self.password, self.phone))
            file.close()
        else:
            file.write("\n")
            file.write(" First_Name: {0} | Last_Name: {1} | E-mail: {2} | Password: {3} | Phone: {4} ".format(self.f_name, self.l_name, self.email,self.password, self.phone))
            file.close()


def first_name_Va():
    first_name = input("Enter Your First Name: ")
    if len(first_name) == 0 or len(first_name) < 3:
       print("Plesae Enter Valid First Name")
       return first_name_Va()
    else:
        return first_name

def last_name_Va ():
    last_name = input("Enter Your last Name: ")
    if len(last_name) == 0 or len(last_name) < 3:
        print("Please Enter Your last Name")
        return last_name_Va()
    else:
        return last_name

def email_V ():
    email = input("Enter Your E-mail: ")
    valid_email = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
    is_match = bool(valid_email)
    if is_match == True:
        return email
    else:
        print("Please Enter A Valid E-mail")
        return email_V()

def mobile_V ():
    mobile = input('enter your mobile number: ')
    if len(mobile) == 12 and mobile[:2] == '20':
        return mobile
    else:
        print('Phone should be 12 number and start with Egypt format (20)')
        return mobile_V()

def password_V ():
    password = input("Enter Your Password: ")
    if len(password) == 0:
        print("Please Enter A Valid Password")
        password_V()
    else:
        confirm_pass = input("Confirm Your Password: ")
        while confirm_pass != password:
            print("Password Doesn't Match")
            confirm_pass = input("Confirm Your Password: ")
            if confirm_pass == password:
                return password
                break
        if confirm_pass == password:
            return password


def get_data_ready():
    USER.write_to_file(USER(first_name_Va(),last_name_Va(),email_V(),mobile_V(),password_V()))
