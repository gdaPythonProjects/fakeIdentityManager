# main file

from cmdinput import cmdInput
from exec.display import Display
from exec.fakeID import fakeID

if __name__ == '__main__':
    Display = Display()
    cmdInput = cmdInput()
    if cmdInput.uArgs == '1':
        fakeID = fakeID()

