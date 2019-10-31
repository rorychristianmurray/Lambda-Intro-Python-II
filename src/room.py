# Implement a class to hold room information. This should have name and
# description attributes.

# Create room class
# give it attributes from adv.py


class Room:
    def __init__(self, name, desc):  # constructor
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"Name: {self.name}\n Desc: {self.desc}\n"


# r = Room("Duskery", "A sad place, really")
# print("r : ", r)
