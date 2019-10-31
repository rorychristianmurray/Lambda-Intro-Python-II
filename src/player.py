# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, desc, room, item):  # constructor
        self.name = name
        self.desc = desc
        self.room = room
        self.item = item

    def __str__(self):
        return f"Name: {self.name}\n Desc: {self.desc}\n Room: {self.room}\n Item: {self.item}\n"
