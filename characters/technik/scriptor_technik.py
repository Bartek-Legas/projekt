from random import randint
import random
class ScriptorTechnik:
    def __init__(self)->None:
        self._unlocked_mistral_strike = True
        self._unlocked_backstap = False
        self._unlocked_hidden_strike = False
    def mistral_strike(self,character):
        if character._mana>=150:
            character._mana-=150
            return 60
        else:
            print("the wasn't enouth mana")
            return 0
    def backstap(self,character):
        if character._mana>=45:
            character._mana-=45
            backstap_demage=5
            backstap_duration=4
            print(f"backstap bulls the enemy for {backstap_demage} demage over {backstap_duration} turns")
            return 50
        else:
            print("the wasn't enouth mana")
            return 0
    def hidden_strike(self,character):
        if character._mana>=55:
            character._mana-=55
            stum_chance=0.4
            stum_efect="stum" if random.random()<stum_chance else None
            print(f"hidden strike deals 35 demage"+ ("stums the enemy" if stum_efect else""))
            return 55
        else:
            print("the wasn't enouth mana")
            return 0
    def choose_technik(self,character):
        while True:
            print(f"a-mistral strike avaible?{self._unlocked_mistral_strike}")
            print(f"b-backstap avaible?{self._unlocked_backstap}")
            print(f"c-hidden strike abaible?{self._unlocked_hidden_strike}")
            print(f"d-exit")
            inp = input().lower()
            if inp == "a" and self._unlocked_mistral_strike:
                return self.mistral_strike(character)
            elif inp == "b" and self._unlocked_backstap:
                return self.backstap(character)
            elif inp == "c" and self._unlocked_hidden_strike:
                return self.hidden_strike(character)
            elif inp == "d":
                print("close technik:)")
                return 0
            else:
                print("this atak has't been unlocked or dasn't exist")
    def unlocked_technik(self,character):
        while True:
            print(f"a-free spell(-150mana,-60hp,{self._unlocked_mistral_strike})")
            print(f"b-500 gold(-45mana,-50hp+bull,{self._unlocked_backstap})")
            print(f"c-800gold(-55mana,-55hp+stum,{self._unlocked_hidden_strike})")
            print(f"d-exit")
            inp = input().lower()
            if(inp=="a" and not self._unlocked_mistral_strike and character._gold>=100):
                self._unlocked_mistral_strike = True
            elif(inp=="b" and not self._unlocked_backstap and character._gold>=500):
                character._gold -= 500
                self._unlocked_backstap = True
            elif(inp=="c" and not self._unlocked_hidden_strike and character._gold>=800):
                character._gold -= 800
                self._unlocked_hidden_strike = True
            elif inp == "d":
                print("you don't have enoth gold")
                break
            else:
                if inp in ["a","b","c"]:
                    print("you don't have enoth gold or you know this atack")
                else:
                    print("this option doesn't exist")

