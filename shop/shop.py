class Shop:
    def __init__(self):
        self.add_hp = 25
        self.add_mana = 50
    def modification(self,character):
        while True:
            try:
                print(f"a - add_hp ({self.add_hp})")
                print(f"b - add_mana ({self.add_mana})")
                print("d - add mana potion")
                print("e - add life potion")
                print("x - exit")
                inp = input().lower()
                if inp == "a" and character._gold>=75:
                    character._gold -= 75
                    character._max_hp += self.add_hp
                    character._hp += self.add_hp
                elif inp == "b" and character._gold>=50:
                    character._gold -= 50
                    character._max_mana += self.add_mana
                    character._mana += self.add_mana
                elif inp == "d" and character._gold >=200:
                    character._gold -= 200
                    character._mana_potion += 1 
                elif inp == "e" and character._gold >= 200:
                    character._gold -= 200
                    character._life_potion += 1
                elif inp == "x":
                    print("exit")
                    break
                else:
                    print("you don't have enoth gold")
            except Exception as e:
                print(f"an error:{e}")
                
                