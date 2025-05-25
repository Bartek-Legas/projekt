from characters.characters import Character 
from random import randint
class Klik(Character):
    def __init__(self):
        super().__init__()
        self._atak = randint(65,70)
        self._max_hp = 65
        self._hp = 65
        self._max_mana = 25
        self._mana = 20
    def fight(self):
        print("----------klik------------")
        super().print_statistic()
        return self._atak
    def drop(self):
        return randint(70,75)
    
