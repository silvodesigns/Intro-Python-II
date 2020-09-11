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

myPlayer = Player("kevin",room["outside"])
direction = ""
# Write a loop that:
while(direction != "quit"):
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    print(myPlayer)
# * Waits for user input and decides what to do.
    print("N = go north, S = go south, E = go east, W = go west")
    direction = input("Where do you wanna go now?")
  
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
    if(direction == "n" and myPlayer.location.name == "Outside Cave Entrance"):
        myPlayer.location = room["foyer"]
    elif(direction == "w" or direction == "e" or direction == "s"
        and myPlayer.location.name == "Outside Cave Entrance"
        ):
        print("Sorry you have hit a wall, nothing in that direction...")
    elif(myPlayer.location.name == "Foyer" and direction == "n"):
        myPlayer.location = room["overlook"]
    elif(myPlayer.location.name == "Foyer" and direction == "e"):
        myPlayer.location = room["narrow"]
    elif(myPlayer.location.name == "Foyer" and direction == "w"):
        print("Sorry you have hit a wall, nothing in that direction...")
    elif(myPlayer.location.name == "Foyer" and direction == "s"):
        myPlayer.location = room["outside"]
    
    elif(myPlayer.location.name == "Grand Overlook" and direction == "s"):
        myPlayer.location = room["foyer"]
    elif(myPlayer.location.name == "Grand Overlook" and direction == "n" \
        or direction == "e" or direction == "w"):
         print("Sorry you have hit a wall, nothing in that direction...")

    elif(myPlayer.location.name == "Narrow Passage" and direction == "n"):
        myPlayer.location.name = room["treasure"]
    elif(myPlayer.location.name == "Narrow Passage" and direction == "s" \
        or direction == "e"):
        print("Sorry you have hit a wall, nothing in that direction...")
    elif(myPlayer.location.name == "Narrow Passage" and direction == "w"):
        myPlayer.location.name == "foyer"

    elif(myPlayer.location.name == "Treasure Chamber" and direction == "s"):
        myPlayer.location.name = room["narrow"]
    elif(myPlayer.location.name == "Treasure Chamber" and direction == "n"\
        or direction == "w" or direction == "e"):
        print("Sorry you have hit a wall, nothing in that direction...")





# If the user enters "q", quit the game.
