from exec.fakeID import fakeID
import random
import numpy as np

class fakeidgen:
    def __init__(self, gender):
        self.name = self.setname(gender)
        self.surName = self.setsurename()
        self.pesel = self.setpesel()
        self.email = self.setemail()

        print(self.name, self.surName)

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
        pass

    def setemail(self):
        pass








