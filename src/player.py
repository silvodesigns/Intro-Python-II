# Write a class to hold player information, e.g. what room they are in
# currently.

#Players should have a name and current_room attributes
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.bag = []

    def __str__(self):
        output = ""
        output += f"{self.location.name}\n"
        output += f"{self.location.description}\n"
        output += f"{self.location}\n"
        output += "Items held: \n"
        for x in self.bag:
            output += x.name + "\n"
            
        return output


    def move(self, direction):
        if self.location.connected_rooms[direction] is not None:
            self.location = self.location.connected_rooms[direction]
        else:
            print("Sorry you have hit a wall, nothing in that direction...")

    def add_item(self, item):
         self.bag.append(item)
    
    def drop_item(self, item_name):
        for i in range(len(self.bag)):
            if self.bag[i].name.lower() == item_name:
                return self.bag.pop(i)
        return None

