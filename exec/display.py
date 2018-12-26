from menu import Menu

class Display:
    def __init__(self):
        dis = Menu()
        self.list = dis.get()
        for i in range(0, len(self.list)):
            if i % 2 == 0:
                print(str(self.list[i]) + ". ", end='')
            else:
                print(self.list[i])
