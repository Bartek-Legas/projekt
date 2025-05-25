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
    hero.regeneration
    while hero.life() and oponent.life():
        hero._reduce_hp(oponent.fight())
        oponent._reduce_hp(hero.fight())
    if not (hero.life()):
        return None
    hero.add_gold(oponent.drop())
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
    choose = [
        ("Echo",500,"b"),
        ("Path",800,"c"),
        ("Ray" ,1000,"d"),
        ("Scriptor" , 1200,"e"),
        ("Vector" , 1500, "f"),
        ("Warior" , 2000, "g"),
        ("Zed" , 2500, "h")
    ]
    print("you can unbolck:")
    for hero,gold,options in choose:
        if not unlocked_characters[hero]:
            print(f"{options} -{hero} ({gold}gold)")
    choose = input("choose hero you can unblock").lower()
    for hero,gold,options in choose:
        if choose == options and not unlocked_characters[hero]:
            if hero._gold>=gold:
                hero._gold-=gold
                unlocked_characters[hero]=True
                print(f"{hero} unblock")
                return
            else:
                print("you don't have enouth gold")
                return
    print("bad choose or hero already unlocked")
def game():
    hero = None
    while not hero:
        hero=choose_hero()
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
                d += 1
            elif choose2 == "b":
                unlocked_characters(hero)
        elif choose == "j":
            hero.reset()
            d += 1
        elif choose == "k":
            hero = choose_hero()
            # shop = choose_shop(hero)
        elif choose == "x":
            print("finish game")
            break
        else:
            print("there is no such comend")
game()
            


