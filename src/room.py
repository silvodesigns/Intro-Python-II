# Implement a class to hold room information. This should have name and
# description attributes.


'''

Put the Room class in room.py based on what you see in adv.py.
The room should have name and description attributes.
The room should also have n_to, s_to, e_to, and w_to attributes which point 
to the room in that respective direction.
'''

class Room:
    def __init__(self,name, description):
        #attributes
        self.name = name
        self.description = description
        self.connected_rooms = {
            "n" : None,
            "s" : None,
            "w" : None,
            "e" : None
        }
        self.items = []

    def __str__(self):
     output = ""
     output += "Items in these room:" + "\n"
     for i in self.items:
           output += "--" + i.name + "\n"
     return output

    def add_item(self, item):
        self.items.append(item)
    
    def search_item(self, item_name):
        for i in self.items:
            if(i.name.lower() == item_name):
                return i
        return None
    
    def remove_item(self, item_name):
        for i in range(len(self.items)):
            if(self.items[i].name.lower() == item_name):
                return self.items.pop(i)
        return None



       



   