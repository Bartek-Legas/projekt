class Shop:
    def __init__(self):
        self.add_hp = 25
        self.add_mana = 50
    def modification(self,character):
        while True:
            try:
                print(f"a - add_hp ({self.add_hp})")
                print(f"b - add_mana ({self.add_mana})")
                inp = input().lower()
                if inp == "a" and character._gold>100:
                    character._gold -= 100
                    character._max_hp += self.add_hp
                if inp == "a" and character._gold>100:
                    character._gold -= 100
                    character._max_hp += self.add_hp
                elif inp == "b" and character._gold>100:
                    character._gold -= 100
                    character._max_mana += self.add_mana
            except Exception as e:
                print(f"an error:{e}")
                