# main file

from cmdinput import cmdInput
from exec.display import Display
from exec.fakeID import fakeID
from exec.fakeIDgenerator import fakeidgen
from exec.api import inputid, delid, showids


if __name__ == '__main__':
    Display = Display()
    cmdInput = cmdInput()
    if cmdInput.uArgs == '1':
        fakeID = fakeID()
        inputid(fakeID.getname(), fakeID.getsurname(), fakeID.getpes(), fakeID.getemail())
    elif cmdInput.uArgs == '2':
        fakeidgen = fakeidgen(input("Enter 1 for female anything for male: "))
        inputid(fakeidgen.getname(), fakeidgen.getsurname(), fakeidgen.getpes(), fakeidgen.getemail())
    elif cmdInput.uArgs == '3':
        showids()
        op = input('1. delete row, \nanything: exit:')
        if op == '1':
            delid(int(input("please enter the line number to be deleted: ")))
        else:
            pass



