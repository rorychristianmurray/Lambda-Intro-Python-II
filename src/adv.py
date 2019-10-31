import argparse
from room import Room

# Declare all the rooms
# uncomment block
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

print("narrow:\n ", room['narrow'])
print("*********\n\n\n*********")
print(room['outside'])
print("*********\n\n\n*********")
print("dir test", room['outside'].n_to)


# Link rooms together

# uncomment block
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

# List
# Create REPL parser which takes one arg [DONE]
# that arg has 4 valid commands, n, s, e, and w [DONE]
# if player moves to occupied room throw an error


# define program description
text = 'This is a text based game'

# initiate the parser
parser = argparse.ArgumentParser(description=text)

parser.add_argument("-V", "--version",
                    help="Shows program version", action="store_true")
parser.add_argument("--width", "-w", help="set output width")

parser.add_argument("direction", help="set direction of character move. Valid moves are n, s, e, and w", choices=[
                    'n', 's', 'e', 'w', 'q'])

# parse args
args = parser.parse_args()
print("args : ", args)

# check for --version or -V
if args.version:
    print("this is myprogram version 0.1")

# check for --width
if args.width:
    print("set output width to %s" % args.width)

d = args.direction
print("d: ", d)


# Make a new player object that is currently in the 'outside' room.

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
