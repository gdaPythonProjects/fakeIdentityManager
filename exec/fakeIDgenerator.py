from exec.fakeID import fakeID
import random
import numpy as np

class fakeidgen:
    def __init__(self):
        self.name = self.setname()
        self.surName = self.setsurename()
        self.pesel = self.setpesel()
        self.email = self.setemail()

    def setname(self):
        with open('name_f.txt') as f:
            names = f.read().splitlines()
        arr = np.asarray(names)
        name = arr[random.randint(0, len(arr))]
        return name

    def setsurename(self):
        pass

    def setpesel(self):
        pass

    def setemail(self):
        pass



def nameRand():




