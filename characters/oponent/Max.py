from characters.characters import Character
from random import randint
class Max(Character):
    def __init__(self):
        super().__init__()
        self._atak = randint(30,35)
        self._max_hp = 70
        self._hp = 70
        self._max_mana = 30
        self._mana = 25
    def fight(self):
        print("----------max------------")
        super().print_statistic()
        return self._atak
    def drop(self):
        return randint(40,45)
    
