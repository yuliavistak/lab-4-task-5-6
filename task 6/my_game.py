class Character:
    """
    Class of all characters of each type
    """
    def __init__(self, name) -> None:
        self.name = name
        self.description = ''
        self.message = ''

    def set_description(self, description):
        self.description = description

    def describe(self):
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

    def add_description(self):
        """
        Adds general information
        """
        self.description += "(If yes, print 'fight')'"

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
        self.description = description

    def set_kind_character(self, person):
        self.kind_character = person

    def get_kind_character(self):
        return self.kind_character

    def set_bad_character(self, person):
        self.bad_character = person

    def get_bad_character(self):
        return self.bad_character

    def get_details(self):
        print(self.description)
        print('--------------------')
        print(self.name + '\n')
