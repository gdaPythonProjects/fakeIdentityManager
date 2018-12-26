# geting arguments from cmd

class cmdInput:
    def __init__(self):
        while True:
            self.uArgs = input("What you want to do?")
            if self.uArgs != "":
                break
            else:
                print("ERROR: You need to write a number")



