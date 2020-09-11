# Write a class to hold player information, e.g. what room they are in
# currently.

#Players should have a name and current_room attributes
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.location.name}" + "\n" + f"{self.location.description}"