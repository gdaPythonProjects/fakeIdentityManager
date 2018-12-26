
class fakeID:
    def __init__(self):
        self.name = self.setname()
        self.surName = self.setsurename()
        self.pesel = self.setpesel()
        self.email = self.setemail()

    def setname(self):
        return input("Enter name: ")

    def setsurename(self):
        return input("Enter surname: ")

    def setpesel(self):
        return input("Enter pesel: ")

    def setemail(self):
        return input("Enter email: ")
