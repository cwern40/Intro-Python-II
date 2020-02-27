from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Sword", "short")]),

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
choice = input("Where do you want to go? Type a cardinal direction (n, s, e, or w): ")

while choice != "q":
    current = ""
    for key, value in room.items():
        if player_1.room == value:
            current = key
    if len(choice.split()) == 1:
        direction = choice.lower() + "_to"
        if hasattr(room[current], str(direction)) == True:
            player_1.room = eval(f'room["{current}"].{direction}')
            print(f'\n{player_1.name} is now in {player_1.room}')
            choice = input("What do you want to do now? Type a cardinal direction (n, s, e, or w) to go to a different room or get/drop (item name) to drop or add an item if available: ")
        else:
            choice = input("invalid selection. Please type a differenct cardinal direction (n, s, e, or w) to go to a different room or get/drop (item name) to drop or add an item if available: ")
    elif len(choice.split()) == 2:
        action = choice.split()[0].lower()
        if action == "get":
            for i in player_1.room.current_items:
                if choice.split()[1].capitalize() == i.name:
                    get_item = i
            player_1.current_items.append(get_item)
            player_1.room.current_items.remove(get_item)
            print(get_item.on_take())
            print(f'\n{player_1.name} now has the following items: {player_1.item_inventory()}and is still in {player_1.room}')           
            choice = input("What do you want to do now? Type a cardinal direction (n, s, e, or w) to go to a different room or get/drop (item name) to drop or add an item if available: ")
        elif action == "drop":
            for i in player_1.current_items:
                if choice.split()[1].capitalize() == i.name:
                    drop_item = i
            player_1.current_items.remove(drop_item)
            player_1.room.current_items.append(drop_item)
            print(drop_item.on_drop())
            print(f'\n{player_1.name} now has the following items: {player_1.item_inventory()}and is still in {player_1.room}')           
            choice = input("What do you want to do now? Type a cardinal direction (n, s, e, or w) to go to a different room or get/drop (item name) to drop or add an item if available: ")
        else:
            choice = input("invalid selection. Please type a differenct cardinal direction (n, s, e, or w) to go to a different room or get/drop (item name) to drop or add an item if available: ")
    else:
        choice = input("invalid selection. Please type a differenct cardinal direction (n, s, e, or w) to go to a different room or get/drop (item name) to drop or add an item if available: ")