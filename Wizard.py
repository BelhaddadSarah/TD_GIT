import random

class Wizard:
    chance = 20
    prix = 15
    type_unite = "wizard"

    def __init__(self) : 
        self.degat = random.choice([2,4])