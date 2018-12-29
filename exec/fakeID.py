from validations.isdigit import is_number
from validations.isemail import emailAddress


class fakeID:
    def __init__(self):
        self.name = self.setname()
        self.surName = self.setsurename()
        self.pesel = self.setpesel()
        self.email = self.setemail()

    def setname(self):
        while True:
            n = input("Enter name: ")
            if str.isupper(n[0]):
                return n
            else:
                print("Name should start with capital letter")


    def setsurename(self):
        while True:
            s = input("Enter surname: ")
            if str.isupper(s[0]):
                return s
            else:
                print("Surname should start with capital letter")

    def setpesel(self):
        while True:
            p = input("Enter pesel: ")
            if is_number(p) and len(p) == 11:
                return p
            else:
                print("Pesel should cantain eleven numbers")

    def setemail(self):
        while True:
            e = input("Enter email: ")
            if emailAddress(e):
                return e
            else:
                print("Wrong email, example: name@name.com")
