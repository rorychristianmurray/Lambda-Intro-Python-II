

class Item:
    def __init__(self, name, desc):  # constructor
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"Weapon: {self.name}\n Desc: {self.desc}\n"
