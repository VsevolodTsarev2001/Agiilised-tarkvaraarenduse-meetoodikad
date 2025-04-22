import random
import json

# --- Sprint 1: Mängija andmed ja põhistruktuur ---
player = {
    "food": 5,
    "energy": 5,
    "health": 10,
    "max_health": 10,
    "inventory": [],
    "location": "kodu",
    "armor": 0,
    "reputation": 0,
    "weapon": None,
    "day": 1,
    "x": 0,
    "y": 0
}

def status():
    print(f"\nPÄEV {player['day']} | Tervis: {player['health']}/{player['max_health']}, Toit: {player['food']}, Energia: {player['energy']}, Asukoht: {player['location']}")
    print(f"Inventar: {', '.join(player['inventory']) if player['inventory'] else 'Tühi'}, Armor: {player['armor']}, Maine: {player['reputation']}, Relv: {player['weapon'] if player['weapon'] else 'Puudub'}")

# --- Sprint 2: Kaart ja liikumine ---
map_grid = {
    (0, 0): "kodu",
    (0, 1): "supermarket",
    (1, 0): "mets",
    (1, 1): "bunkri sissepääs",
    (0, -1): "vangla",
    (-1, 0): "tööstusala"
}

def move():
    direction = input("Vali suund (n, s, e, w): ")
    if direction == 'n': player['y'] += 1
    elif direction == 's': player['y'] -= 1
    elif direction == 'e': player['x'] += 1
    elif direction == 'w': player['x'] -= 1
    else:
        print("Tundmatu suund")
        return
    location = map_grid.get((player['x'], player['y']), "tundmatu ala")
    player['location'] = location
    print(f"Sa liikusid ja oled nüüd: {location}")
    player['energy'] -= 1

# --- Sprint 3: NPC-d ja kauplemine ---
npcs = {
    (0, 1): {"nimi": "Ellujääja Marko", "kaubad": {"ravimikomplekt": 1, "konserv": 2}},
    (-1, 0): {"nimi": "Kaupmees Liis", "kaubad": {"armor": 5, "relv": 10}}
}

def trade():
    pos = (player['x'], player['y'])
    if pos in npcs:
        npc = npcs[pos]
        print(f"Kohtusid: {npc['nimi']}")
        print("Kaubad saadaval:")
        for item, cost in npc['kaubad'].items():
            print(f" - {item}: {cost} toitu")
        valik = input("Mida soovid osta? ")
        if valik in npc['kaubad']:
            if player['food'] >= npc['kaubad'][valik]:
                player['food'] -= npc['kaubad'][valik]
                if valik == "relv":
                    player['weapon'] = "püstol"
                elif valik == "armor":
                    player['armor'] += 2
                else:
                    player['inventory'].append(valik)
                print(f"Ostsid: {valik}")
            else:
                print("Sul pole piisavalt toitu!")
        else:
            print("Ese puudub nimekirjas.")
    else:
        print("Siin pole kedagi, kellega kaubelda.")

# --- Sprint 4: Vaenlased (AI) ---
class Enemy:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self):
        print(f"{self.name} ründab sind!")
        return self.damage

    def take_damage(self, dmg):
        self.health -= dmg
        print(f"{self.name} kaotas {dmg} elu.")
        if self.health <= 0:
            print(f"{self.name} on alistatud!")
            return True
        return False

# --- Sprint 5: Salvestamine ja laadimine ---
def save_game():
    with open("savegame.json", "w") as f:
        json.dump(player, f)
    print("Mäng salvestatud!")

def load_game():
    global player
    try:
        with open("savegame.json", "r") as f:
            player = json.load(f)
        print("Mäng laaditud!")
    except:
        print("Salvestatud mängu ei leitud.")

# --- Sprint 6: Käsitöö (crafting) ---
crafting_recipes = {
    "superkomplekt": ["ravimikomplekt", "konserv"],
    "soomusjakk": ["armor", "ravimikomplekt"]
}

def craft():
    print("Saadaval retseptid:")
    for item, components in crafting_recipes.items():
        print(f" - {item}: {', '.join(components)}")
    valik = input("Mida soovid meisterdada? ")
    if valik in crafting_recipes:
        if all(c in player['inventory'] for c in crafting_recipes[valik]):
            for c in crafting_recipes[valik]:
                player['inventory'].remove(c)
            player['inventory'].append(valik)
            print(f"Meisterdasid eseme: {valik}")
        else:
            print("Sul pole piisavalt komponente.")
    else:
        print("Tundmatu ese.")

# --- Sprint 7: Mängutsükkel ja kaotuse tingimused ---
def check_game_over():
    if player['health'] <= 0:
        print("Sa surid. Mäng läbi.")
        return True
    if player['energy'] <= 0 and player['food'] == 0:
        print("Sa nälgisid ja sul puudus energia liikumiseks. Mäng läbi.")
        return True
    return False

def game_loop():
    print("Tere tulemast ellujäämismängu 'Sundöö'!")
    while True:
        status()
        print("\nValikud: (1) Liigu, (2) Kaubelda, (3) Meisterda, (4) Salvestus, (5) Laadi, (6) Puhka, (7) Välju")
        valik = input("Tee oma valik: ")

        if valik == '1':
            move()
        elif valik == '2':
            trade()
        elif valik == '3':
            craft()
        elif valik == '4':
            save_game()
        elif valik == '5':
            load_game()
        elif valik == '6':
            if player['food'] > 0:
                player['food'] -= 1
                player['energy'] = min(player['energy'] + 3, 5)
                print("Sa puhkasid ja taastasid energiat.")
            else:
                print("Sul pole toitu puhkamiseks.")
        elif valik == '7':
            print("Väljud mängust. Nägemist!")
            break
        else:
            print("Tundmatu käsklus.")

        if check_game_over():
            break

        player['day'] += 1

# Käivita mäng
if __name__ == "__main__":
    game_loop()