# main file

from cmdinput import cmdInput
from exec.display import Display
from exec.fakeID import fakeID
from exec.fakeIDgenerator import fakeidgen
from exec.api import inputid

if __name__ == '__main__':
    Display = Display()
    cmdInput = cmdInput()
    if cmdInput.uArgs == '1':
        fakeID = fakeID()
        inputid(fakeID.getAll())
    else:
        fakeidgen = fakeidgen(input("Enter 1 for female anything for male: "))
        inputid(fakeidgen.getname(), fakeidgen.getsurname(), fakeidgen.getpes(), fakeidgen.getemail())
