from characters.characters import Character
from random import randint
class Skeleton(Character):
    def __init__(self):
        super().__init__()
        self._atak = randint(10,15)
        self._max_hp = 60
        self._hp = 60
        self._max_mana = 20
        self._mana = 15
    def fight(self):
        print("----------skeleton------------")
        super().print_statistic()
        return self._atak
    def drop(self):
        return randint(10,20)
    
