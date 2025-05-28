class Character:
    def __init__(self) -> None:
        self._life = True
        self._gold = 200
        self._atak = 0
        self._hp = 0
        self._max_hp = 0
        self._regeneration_hp = 0
        self._mana = 0
        self._max_mana = 0
        self._regeneration_mana = 0 
        self._reduce_hp = 0
    def basic_atak(self):
        return self._atak
    def life (self):
        return self._hp>0
    def regeneration(self):
        if self._hp + self._regeneration_hp>self._max_hp:
            self._hp = self._max_hp
        else: 
            self._hp += self._regeneration_hp
        if self._mana + self._regeneration_mana>self._max_mana:
            self._mana = self._max_mana
        else: 
            self._mana += self._regeneration_mana
    def gold(self,gold):
        self._gold += gold
    def damage(self,damage):
        self._hp -= damage
    def drop(self):
        return self._gold
    def reset(self):
        self._hp = self._max_hp
        self._mana = self._max_mana
    def print_statistic(self):
        print("--------------------------------")
        print(f"max_hp = {self._max_hp} max_mana = {self._max_mana}")
        print(f"hp = {self._hp} mana = {self._mana}")
        print("--------------------------------")
        