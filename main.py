from modules.register import get_data_ready as register
from modules.login import valid_data

def main():
    print("Enter (R) To Register, Enter (L) To Login ")
    choise = input("Your Choise is: ")
    if choise.lower()=="r":
        register()
    elif choise.lower() == "l":
        valid_data()
    else:
        print("Wrong Choise")
        return main()
main()


