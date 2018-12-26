from menu import Menu

class Display:
    def __init__(self):
        dis = Menu()
        self.list = dis.get()
        print(self.list)

