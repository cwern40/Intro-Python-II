from room import Room
from player import Player
from item import Item

# Declare all the rooms
sword = Item("Sword", "short")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [sword]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player("The Guardian", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(player_1)
choice = input("Where do you want to go? (use the cardinal direction n, s, e, or w): ")
direction = choice.lower() + "_to"
action = choice.lower().split()[0]
print(action)
while choice != "q":
    current = ""
    for key, value in room.items():
        if player_1.room == value:
            current = key
    if hasattr(room[current], str(direction)) == True:
        player_1.room = eval(f'room["{current}"].{direction}')
        print(f'\n{player_1.name} is now in {player_1.room}')
        choice = input("Where do you want to go now? (use the Cardinal direction n, s, e, or w): ")
        direction = choice + "_to"
        action = choice.lower().split()[0]
    elif action == "drop" or action == "get":
        choice = input("Where do you want to go now? (use the Cardinal direction n, s, e, or w): ")
        direction = choice + "_to"
        action = choice.lower().split()[0]
    else:
        choice = input("invalid selection. Please choose a differenct cardinal direction (n, s, e, or w): ")
        direction = choice + "_to"