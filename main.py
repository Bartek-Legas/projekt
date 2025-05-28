from all_inport import *
select_characters = ['Ninja',"Echo","Path","Ray","Scriptor","Vector","Warior","Zed"]
unlocked_characters = {
    "Ninja": True,
    "Echo" : False,
    "Path" : False,
    "Ray" : False,
    "Scriptor" : False,
    "Vector" : False,
    "Warior" : False,
    "Zed" : False
}
def one_fight(hero:Ninja | Echo | Patch | Ray | Scriptor | Vector | Warior | Zed ,enemy):
    if enemy == "a":
        oponent = Skeleton()
    elif enemy == "b":
        oponent = Klik() 
    elif enemy == "c":
        oponent = Lex()
    elif enemy == "d":
        oponent = Max()
    elif enemy == "e":
        oponent = Nix()
    elif enemy == "f":
        oponent = Robo()
    elif enemy == "g":
        oponent = Zip()
    elif enemy == "h":
        oponent = Leo()
    oponent.regeneration()
    hero.regeneration()
    while hero.life() and oponent.life():
        hero.damage(oponent.fight())
        oponent.damage(hero.fight())
    if not (hero.life()):
        return None
    hero.gold(oponent.drop())
def choose_shop(hero):
    if isinstance(hero,Ninja):
        shop = NinjaShop()
    elif isinstance(hero,Echo):
        shop = EchoShop()
    elif isinstance(hero,Patch):
        shop = PathShop()
    elif isinstance(hero,Ray):
        shop = RayShop()
    elif isinstance (hero,Scriptor):
        shop = ScriptorShop()
    elif isinstance (hero,Vector):
        shop = VectorShop()
    elif isinstance (hero,Warior):
        shop = WariorShop()
    elif isinstance (hero,Zed):
        shop = ZedShop()
    return shop
def choose_hero():
    for hero,avaible in unlocked_characters.items():
        if avaible:
            print(hero)
    choose = input("hero name").capitalize()
    hero = {
        "Ninja": Ninja,
        "Echo" : Echo,
        "Path" : Patch,
        "Ray" : Ray,
        "Scriptor" : Scriptor,
        "Vector" : Vector,
        "Warior" : Warior,
        "Zed" : Zed
    }
    if choose in hero and unlocked_characters[choose]:
        return hero [choose]()
    print("bad choose or hero blocked")
    return None
def unlocked_hero(hero):                        
    unlock_options = [
        ("Echo", 500, "b"),
        ("Path", 800, "c"),
        ("Ray", 1000, "d"),
        ("Scriptor", 1200, "e"),
        ("Vector", 1500, "f"),
        ("Warior", 2000, "g"),
        ("Zed", 2500, "h")
    ]

    print("You can unlock:")
    for hero_name, gold_cost, option_key in unlock_options:
        if not unlocked_characters[hero_name]:
            print(f"{option_key} - {hero_name} ({gold_cost} gold)")

    choice = input("Choose hero to unlock: ").lower()

    for hero_name, gold_cost, option_key in unlock_options:
        if choice == option_key and not unlocked_characters[hero_name]:
            if hero._gold >= gold_cost:
                hero._gold -= gold_cost
                unlocked_characters[hero_name] = True
                print(f"{hero_name} unlocked!")
                return
            else:
                print("You don't have enough gold.")
                return
    print("Invalid choice or hero already unlocked.")

def game():
    hero = None
    while not hero:
        hero=choose_hero()
    shop = choose_shop(hero)
    d = 1 
    while hero.life():
        print(f"day {d}")
        print("a-h:fight | i city | j rest | k change hero |  x exit")
        hero.inf()
        choose = input().lower()
        if choose in "abcdefgh":
            one_fight(hero,choose)
        elif choose == "i":
            print("a-shop | b-unbolck new hero")
            choose2 = input().lower()
            if choose2 == "a":
              shop = shop.modification(hero) 
            elif choose2 == "b":
                unlocked_hero(hero)
        elif choose == "j":
            hero.reset(hero)
            d += 1
        elif choose == "k":
            hero = choose_hero()
            shop = choose_shop(hero)
        elif choose == "x":
            print("finish game")
            break
        else:
            print("there is no such comend")
game()
            


