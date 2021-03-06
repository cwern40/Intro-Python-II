class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'\nYou have picked up a {self.name}.')

    def on_drop(self):
        print(f'You have dropped a {self.name}.')

    def __str__(self):
        return f'{self.name}'