from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

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
p = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
directions = {
    'n': 'n_to',
    's': 's_to',
    'e': 'e_to',
    'w': 'w_to',
    'north': 'n_to',
    'south': 's_to',
    'west': 'w_to',
    'east': 'e_to'
}

def get_new_room(p, inp):
    try:
        return getattr(p.current_room, directions[inp])
    except KeyError:
        print("That's not a direction you mug")
        return False
    except AttributeError:
        print("You canne go that way")
        return False

def print_details(p):
    print("Current location: ", p.current_room.name)
    print("What's going on here: ", p.current_room.description)


for i in range(10):
    print_details(p)

    inp = input('Where go?: ')

    if inp == 'q':
        break

    new_room = get_new_room(p, inp)

    if new_room:
        p.current_room = new_room

    if i == 9:
        print("You've been ferreting around too long, game over.")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.s
