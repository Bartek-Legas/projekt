from characters.characters import Character
from random import randint
class Nix(Character):
    def __init__(self):
        super().__init__()
        self._atak = randint(25,30)
        self._max_hp = 80
        self._hp = 80
        self._max_mana = 40
        self._mana = 35
    def fight(self):
        print("----------nix------------")
        super().print_statistic()
        return self._atak
    def drop(self):
        return randint(30,35)
    