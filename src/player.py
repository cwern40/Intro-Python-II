# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, current_items = [""]):
        self.name = name
        self.room = room
        self.current_items = current_items

    def __str__(self):
        return f'{self.name} has the following items: {self.current_items} and is in {self.room}'