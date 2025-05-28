from shop.shop import Shop 
from characters.technik.ninja_technik import NinjaTechnik
class PathShop(Shop):
    def __init__(self):
        super().__init__()
        self.add_life = 50
        self.add_mana = 100
    def choose_modification(self, character):
        while True:
            try:
                print(f"a \t Add health ? | - 75 gold | + {self.add_life} hp")
                print(f"b \t Add mana ? | - 50 gold | + {self.add_mana} mana")
                print(f"c \t Add spell")
                print(f"d \t Add mana potion | - 200 gold | + 100 hp | ")
                print(f"e \t Add health potion | - 200 gold | + 100 hp |")
                print(f"x \t Quit the shop")
                inp = input().lower()
                if inp == "a" and character._gold > 75:
                    character._gold -= 75
                    character._max_hp += self.add_life

                elif inp == "b" and character._gold > 50:
                    character._gold -= 50
                    character._max_mana += self.add_mana
                elif inp == "c":
                    character._spell_book.unlock_spells(character)
                elif inp == "d" and character._gold > 200:
                    character._gold -= 200
                    character._mana_potion += 1
                elif inp == "e" and character._gold > 200:
                    character._gold -= 200
                    character._life_potion += 1
                elif inp == "x":
                    print("--- Quit the shop ---")
                    break
                else:
                    print("--- Not enough gold ---")
            except Exception as e:
                print(f"An error occurred: {e}")


