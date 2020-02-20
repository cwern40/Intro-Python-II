# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, current_items = []):
        self.name = name
        self.room = room
        self.current_items = current_items

    def __str__(self):
        output = f'{self.name} has the following items: '
        if int(len(self.current_items)) == 0:
            output += f'None, and is in {self.room}'
        else:
            for i in self.current_items:
                output += f'{i}, and is in {self.room}'
        return output