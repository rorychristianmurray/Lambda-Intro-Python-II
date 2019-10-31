# Implement a class to hold room information. This should have name and
# description attributes.

# Create room class
# give it attributes from adv.py
# give it methods


class Room:
    def __init__(self, name, desc):  # constructor
        self.name = name
        self.desc = desc
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""

    def __str__(self):
        return f"Name: {self.name}\n Desc: {self.desc}\n North takes you: {self.n_to}\n South takes you: {self.s_to}\n East takes you: {self.e_to}\n West takes you: {self.w_to}\n"

    # def n.to(self):
    #     print("The North remembers")

    # def s.to(self):
    #     print("The sun never sets on the southern English empire")

    # def e.to(self):
    #     print("The sun also rises")

    # def w.to(self):
    #     print("Go west young man")


# r = Room("Duskery", "A sad place, really")
# print("r : ", r)
