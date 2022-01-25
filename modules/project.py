import datetime

class PROJECT:
    def __init__(self, title, details, total_target,start_date,end_date):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date

    def write_to_file (self):
        get_data = open("projects.txt", 'r').read()
        file = open("projects.txt", 'a+')
        if len(get_data) < 0:
            file.write("Title: {0} | Details: {1} | Target: {2} | Start Date: {3} | End Date: {4}".format(self.title,self.details,self.total_target,self.start_date,self.end_date))
            file.close()
        else:
            file.write("\n")
            file.write("Title: {0} | Details: {1} | Target: {2} | Start Date: {3} | End Date: {4}".format(self.title,self.details,self.total_target,self.start_date,self.end_date))
            file.close()


def project_Menue():
    print("Enter (1) To List Projects, Enter (2) To Add Project ")
    choise = input("Your Choise is: ")
    if choise == "1":
        list()
    elif choise == "2":
        add_project()
    else:
        print("Wrong Choise")
        return project_Menue()

def list():
    with open("projects.txt") as file:
        all_of_it = file.read()
        print(all_of_it)


def add_project():
    title = input("Please Enter Project Title: ")
    details = input("Please Enter Project Details: ")
    total_target = input("Please Enter Project Total target: ")
    startyear = int(input('Enter Start Year: '))
    startmonth = int(input('Enter Start Month: '))
    startday = int(input('Enter Start Day: '))
    startdate = datetime.date(startyear, startmonth, startday)
    endyear = int(input('Enter End Year: '))
    endmonth = int(input('Enter End Month: '))
    endday = int(input('Enter a End Day: '))
    enddate = datetime.date(endyear, endmonth, endday)
    while enddate < startdate or enddate < datetime.date.today():
        print("Please Enter A Vaild End Date")
        endyear = int(input('Enter End Year'))
        endmonth = int(input('Enter End Month'))
        endday = int(input('Enter End Day'))
        enddate = datetime.date(endyear, endmonth, endday)
    start_date =("{0}-{1}-{2}").format(startday , startmonth , startyear)
    end_date = ("{0}-{1}-{2}").format(endday, endmonth, endyear)

    PROJECT.write_to_file(PROJECT(title,details,total_target,start_date,end_date))

project_Menue()