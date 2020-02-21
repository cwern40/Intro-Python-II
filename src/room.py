# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, current_items = []):
        self.name = name
        self.description = description
        self.current_items = current_items

    def item_inventory(self):
        if int(len(self.current_items)) == 0:
            output = "None"
        else:
            for i in self.current_items:
                output = f'{i}, '
        return output

    def __str__(self):
        output = f'The {self.name}. {self.description}. Current Items in room: '
        if int(len(self.current_items)) == 0:
            output += "None"
        else:
            for i in self.current_items:
                output += f'{i}, '
        return output