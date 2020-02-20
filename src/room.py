# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, current_items = [""]):
        self.name = name
        self.description = description
        self.current_items = current_items

    def __str__(self):
        return f'The {self.name}. {self.description}. Current Items in room: {self.current_items}'