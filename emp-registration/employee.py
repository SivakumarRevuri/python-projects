
class Employee:
    def __init__(self):
        self.position = None
        self.contact = None
        self.dob = None
        self.address = None
        self.mail = None
        self.gender = None
        self.firstname = None
        self.lastname = None
        self.doj = None

    def get_firstname(self):
        return self.firstname

    def set_firstname(self, firstname):
        self.firstname = firstname
        
    def get_lastname(self):
        return self.lastname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_mail(self):
        return self.mail

    def set_mail(self, mail):
        self.mail = mail

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        self.dob = dob

    def get_doj(self):
        return self.doj

    def set_doj(self, doj):
        self.doj = doj

    def __str__(sl) -> str:
        print(sl.firstname,sl.lastname,sl.position,sl.gender,sl.dob,sl.doj,sl.mail, sl.address)

#    address='bgl', position='erhre','rthr', 'rehe'
# emp = Employee(firstname='siva', lastname ='kumar', gender='male', mail='srevuri@gmail.com',address='bgl',
#                position='dev', doj='iui', dob='uirt')
# print(emp)
