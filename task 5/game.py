"""
Description of every character, item or place
"""
class Item:
    """
    Item description
    """
    def __init__(self, name):
        self.name = name
        self.description  = ''
    def set_description(self, message):
        """
        Describes the item in text
        """
        self.description  = message
    def get_name(self):
        """
        Returns name of item
        """
        return self.name
    def describe(self):
        """
        Returns item description in text
        """
        print(f"The [{self.name}] is here - {self.description}")

class Room:
    """
    Room description
    """
    def __init__(self, name):
        self.name = name
        self.character = None
        self.direction = {}
        self.description = ''
        self.item = None

    def set_description(self, message):
        """
        Describes the room
        """
        self.description = message

    def link_room(self, other, direction):
        """
        Determines which rooms are nearby and where they are located
        """
        self.direction[direction] = other

    def set_character(self, other):
        """
        Sets the character in the room
        """
        self.character = other

    def set_item(self, item: Item):
        """
        Sets the item in the room
        """
        self.item = item

    def get_details(self):
        """
        Prints information about the room
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        drct = self.direction
        for direct, room in drct.items():
            print(f"The {room.name} is {direct}")

    def get_character(self):
        """
        Determines if there is the enemy and who he/she is
        """
        return self.character

    def get_item(self):
        """
        Determines if there is the item and what it is
        """
        return self.item

    def move(self, command):
        """
        Moves to another room
        """
        return self.direction[command]

class Enemy:
    """
    Enemy description
    """
    victories = 0
    def __init__(self, name, monster):
        super().__init__()
        self.name = name
        self.stranger = monster
        self.conversation = None
        self.weakness = None

    def set_conversation(self, message):
        """
        Sets conversation of character
        """
        self.conversation = message

    def set_weakness(self, thing):
        """
        Sets weakness of character
        """
        self.weakness = thing

    def describe(self):
        """
        Gives information about the enemy in text 
        """
        print(f"{self.name} is here!")
        print(self.stranger)

    def talk(self):
        """
        Conversation with the enemy 
        """
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, fight_with):
        """
        Victorious battle with enemy
        """
        if fight_with == self.weakness:
            print(f"You fend {self.name} off with the {self.weakness}")
            Enemy.victories += 1
            return True
        return False

    def get_defeated(self):
        """
        Calculates number of user's victories
        """
        return Enemy.victories
