from characters.characters import Character
from characters.technik.vector_technik import VectorTechnik
class Vector(Character):
    def __init__(self):
        super().__init__()
        self._atak += 20
        self._hp = 155
        self._max_hp = 155
        self._regeneration_hp = 10
        self._mana = 505
        self._max_mana = 505
        self._regeneration_mana = 15
        self._mana_potion = 0
        self._life_potion = 0 
        self._spell_book = VectorTechnik()
    def inf(self):
        print("-----------------your statistic----------------------")
        print(f"max_hp = {self._max_hp} max_mana = {self._max_mana}")
        print(f"hp = {self._hp} mana = {self._mana}")
        print(f"gold = {self._gold}")
    def mana_potion(self):
            if self._mana_potion>0:
                self._mana_potion -= 1
                self._mana += 200
            else:
                print("you don't have mana potion")
    def life_potion(self):
            if self._life_potion>0:
                self._life_potion -= 1
                self._hp += 100
            else:
                print("you don't have life potion")
    def fight(self):
        while True:
            self.inf()
            print("a - atak(-20hp)")
            print("b - open vector technik")
            print("c - use mana potion")
            print("d - use life potion")
            demage = 0 
            inp = input().lower()
            if inp == "c":
                self.mana_potion()
                continue
            elif inp == "d":
                self.life_potion()
                continue
            if inp == "a":
                demage = self._atak
            elif inp == "b":
                demage = self._spell_book.choose_technik(self)
            else:
                print("no atak")
                continue
            return demage
        