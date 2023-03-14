"""
Class for game "blukachka in Drohobych"
"""
class Character:
    """
    Class of all characters of each type
    """
    def __init__(self, name) -> None:
        self.name = name
        self.description = ''
        self.message = ''

    def set_description(self, description):
        """
        Adds description of character
        """
        self.description = description

    def describe(self):
        """
        Describes character in text
        """
        print(f"{self.name} is here!")
        print("~~~~~~~~~~~~")
        print(self.description)

class Killer(Character):
    """
    Enemy who would fight with you
    """
    def __init__(self, name, item) -> None:
        super().__init__(name)
        self.weakness = item

    def fight(self, fight_with):
        """
        Determines if the fight is victorious
        """
        return fight_with == self.weakness

class Zbuj(Character):
    """
    Enemy who robbs the rich
    """
    def __init__(self, name, item) -> None:
        super().__init__(name)
        self.stolen = item

class KindLaydak(Character):
    """
    Gives the user hint
    """
    def __init__(self, name) -> None:
        super().__init__(name)
        self.need = 'gold'
        self.hint = None

    def set_hint(self, hint):
        """
        Adds a hint that person says
        """
        self.hint = hint

class Kavaler(Character):
    """
    Helps you win the killer
    """
    def __init__(self, name, number) -> None:
        super().__init__(name)
        self.number = number


class Street:
    """
    Locations of game
    """
    def __init__(self, name):
        self.name = name
        self.description = ''
        self.kind_character = None
        self.bad_character = None

    def set_description(self, description):
        """
        Adds description of the street
        """
        self.description = description

    def set_kind_character(self, person):
        """
        Adds kind charcter on the street
        """
        self.kind_character = person

    def get_kind_character(self):
        """
        Determines if there is a kind character
        """
        return self.kind_character

    def set_bad_character(self, person):
        """
        Adds bad charcter on the street
        """
        self.bad_character = person

    def get_bad_character(self):
        """
        Determines if there is a bad character
        """
        return self.bad_character

    def get_details(self):
        """
        Describes street in text
        """
        print(self.description)
        print('--------------------')
        print(self.name + '\n')
