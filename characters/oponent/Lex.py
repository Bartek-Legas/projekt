from characters.characters import Character 
from random import randint
class Lex(Character):
    def __init__(self):
        super().__init__()
        self._atak = randint(50,55)
        self._max_hp = 75
        self._hp = 75
        self._max_mana = 35
        self._mana = 30
    def fight(self):
        print("----------lex------------")
        super().print_statistic()
        return self._atak
    def drop(self):
        return randint(60,65)
    
