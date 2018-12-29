# getting arguments from cmd

class cmdInput:
    def __init__(self):
        while True:
            self.uArgs = input("Choose option: ")
            if self.uArgs != "":
                break
            else:
                print("ERROR: You need to write a number")

