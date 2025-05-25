from characters.characters import Character 
from random import randint
class Leo(Character):
    def __init__(self):
        super().__init__()
        self._atak = randint(60,65)
        self._max_hp = 80
        self._hp = 80
        self._max_mana = 55
        self._mana = 45
    def fight(self):
        print("----------leo------------")
        super().print_statistic()
        return self._atak
    def drop(self):
        return randint(80,85)
    