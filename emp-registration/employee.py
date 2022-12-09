
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
        self.cntry = None

    # def __int__(self, firstname: str, lastname: str, gender: str, mail: str, contact: int, address: str, position: str,
    #             dob, doj, cntry: str):
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.gender = gender
    #     self.mail = mail
    #     self.contact = contact
    #     self.address = address
    #     self.position = position
    #     self.dob = dob
    #     self.doj = doj
    #     self.cntry = cntry

    @property
    def get_firstname(self):
        return self.firstname

    @get_firstname.setter
    def set_firstname(self, firstname):
        self.firstname = firstname

    @property
    def get_lastname(self):
        return self.lastname

    @get_lastname.setter
    def set_lastname(self, lastname):
        self.lastname = lastname

    @property
    def get_gender(self):
        return self.gender

    @get_gender.setter
    def set_gender(self, gender):
        self.gender = gender

    @property
    def get_mail(self):
        return self.mail

    @get_mail.setter
    def set_mail(self, mail):
        self.mail = mail

    @property
    def get_contact(self):
        return self.contact

    @get_contact.setter
    def set_contact(self, contact):
        self.contact = contact

    @property
    def get_address(self):
        return self.address

    @get_address.setter
    def set_address(self, address):
        self.address = address

    @property
    def get_position(self):
        return self.position

    @get_position.setter
    def set_position(self, position):
        self.position = position

    @property
    def get_dob(self):
        return self.dob

    @get_dob.setter
    def set_dob(self, dob):
        self.dob = dob

    @property
    def get_doj(self):
        return self.doj

    @get_doj.setter
    def set_doj(self, doj):
        self.doj = doj

    @property
    def get_cntry(self):
        return self.cntry

    @get_cntry.setter
    def set_cntry(self, cntry):
        self.cntry = cntry
