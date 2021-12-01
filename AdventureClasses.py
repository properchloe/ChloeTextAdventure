class Character():
    """ Class to hold stats for any living being in the game. """

    def __init__(self, name, inventory = []): #can you do default values in class inits?
        self.name = name
        self.inventory = inventory


class Player(Character):
    """ Class to hold information for the player character. """

    #


class Item():
    """ Class to hold information for interactable objects in-game. """

    def __init__(self):
        #


class Weapon(Item):
    """ Class to hold information about weapons for combat. """

    #


class Container():
    """ Class to hold information about containers that hold items. """

    def __init__(self):
        #
