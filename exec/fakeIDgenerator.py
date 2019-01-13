from exec.fakeID import fakeID
import random
import string
import numpy as np

class fakeidgen:
    def __init__(self, gender):
        self.name = self.setname(gender)
        self.surName = self.setsurename()
        self.pesel = self.setpesel()
        self.email = self.setemail()

        print(self.name, self.surName, self.pesel, self.email)

    def setname(self, gender):
        if gender == 1:
            with open('exec/name_f.txt') as f:
                names = f.read().splitlines()
                f.close()
        else:
            with open('exec/name_m.txt') as f:
                names = f.read().splitlines()
                f.close()
        arr = np.asarray(names)
        name = arr[random.randint(0, len(arr))]
        return name


    def setsurename(self):
        with open('exec/surname.txt') as f:
            names = f.read().splitlines()
        arr = np.asarray(names)
        name = arr[random.randint(0, len(arr))]
        return name


    def setpesel(self):
        value = ""
        for i in range(0, 11):
            value = value + str(random.randint(0, 9))
        return value


    def setemail(self):
        value1 = ""
        value2 = ""
        for i in range(0, random.randint(5, 10)):
            value1 = value1 + random.choice(string.ascii_lowercase)
            value2 = value2 + random.choice(string.ascii_lowercase)
        return value1 + "@" + value2 + ".com"

    def getname(self):
        return self.name

    def getsurname(self):
        return self.surName

    def getpes(self):
        return self.pesel

    def getemail(self):
        return self.email







