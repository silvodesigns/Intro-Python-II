from room import Room
from player import Player
from items import Items


#items

sword = Items("Sword","A powerful and deadly sword")
potion = Items("Potion", "Recovers a little bit of health")
shield = Items("Shield", "Protects you from light hits")



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

room['outside'].connected_rooms["n"] = room['foyer']
room['foyer'].connected_rooms["s"] = room['outside']
room['foyer'].connected_rooms["n"] = room['overlook']
room['foyer'].connected_rooms["e"]= room['narrow']
room['overlook'].connected_rooms["s"] = room['foyer']
room['narrow'].connected_rooms["w"]= room['foyer']
room['narrow'].connected_rooms["n"] = room['treasure']
room['treasure'].connected_rooms["s"] = room['narrow']

#add items

room['outside'].add_item(sword)
room['foyer'].add_item(potion)
room['narrow'].add_item(shield)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

myPlayer = Player("kevin",room["outside"])
command = ""
# Write a loop that:
while(command != "quit"):
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    print(myPlayer)
    if myPlayer.location.name == "Treasure Chamber":
        break
# * Waits for user input and decides what to do.
    print("N = go north, S = go south, E = go east, W = go west\n")
    print("Take items name or Drop items name")
    command = input("Where do you wanna go now?")
  
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

    
    if command in set("nesw"):
        myPlayer.move(command)
    if len(command) > 1:
        info = command.split()
        term = ""
        if info[0].lower() == "take" or "get":
            if myPlayer.location.search_item(info[1].lower()):
                myPlayer.add_item(myPlayer.location.search_item(info[1].lower()))
                print(f"The item {info[1]} has been added")
                myPlayer.location.remove_item(info[1].lower())
        else:
            print("The item asking for not here")
        
        if info[0].lower() == "drop":
            item = myPlayer.drop_item(info[1])
            if item:
                myPlayer.location.add_item(item)
                print(f"Item {info[1]} has been added to the room")
            else: 
                print("Item u wanna drop u dont have")
        
           


     

   

# If the user enters "q", quit the game.
