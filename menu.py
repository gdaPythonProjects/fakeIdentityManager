#menu options

class Menu:
    def __init__(self):
        self.menuList = (
            1, "Create new identity",
            2, "Create new random identity automatically",
            3, "Show created identities "
        )

    def get(self):
        return self.menuList
