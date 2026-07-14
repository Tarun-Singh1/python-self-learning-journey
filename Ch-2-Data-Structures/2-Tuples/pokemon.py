import random
from collections import namedtuple


Pokemon = namedtuple("Pokemon", ["name", "hp", "attack", "defense", "moves"])
pokedex = [
    Pokemon("Pikachu", 100, 85, 40, [("Thunderbolt", 90, 100), ("Quick Attack", 40, 100), ("Thunder", 110, 70)]),
    Pokemon("Charizard", 120, 95, 60, [("Flamethrower", 90, 100), ("Slash", 70, 100), ("Fire Blast", 110, 70)]),
    Pokemon("Blastoise", 130, 75, 90, [("Hydro Pump", 110, 80), ("Surf", 90, 100), ("Bite", 60, 100)]),
    Pokemon("Gengar", 90, 110, 35, [("Shadow Ball", 80, 100), ("Sludge Bomb", 90, 100), ("Hypnosis", 0, 60)])
]

print("--- POKÉMON BATTLE SELECT ---")
for i, p in enumerate(pokedex):
    print(f"{i + 1}. {p.name} (HP: {p.hp}, ATK: {p.attack}, DEF: {p.defense})")

idx1 = int(input("Player 1, pick your Pokémon (1-4): ")) - 1
idx2 = int(input("Player 2, pick your Pokémon (1-4): ")) - 1

p1 = pokedex[idx1]
p2 = pokedex[idx2]
hp1 = p1.hp
hp2 = p2.hp
turn = 0  # 0 for P1, 1 for P2

print(f"\nBattle: {p1.name} vs {p2.name}")

while hp1 > 0 and hp2 > 0:
    if turn == 0:
        attacker = p1
        defender_hp = hp2
        print(f"\nPlayer 1's Turn ({attacker.name} HP: {hp1})")
    else:
        attacker = p2
        defender_hp = hp1
        print(f"\nPlayer 2's Turn ({attacker.name} HP: {hp2})")

    for i, move in enumerate(attacker.moves):
        # Unpack tuple directly
        m_name, m_power, m_acc = move
        print(f"{i + 1}. {m_name} | Power: {m_power} | Accuracy: {m_acc}%")

    choice = int(input("Select move: ")) - 1

    name, power, acc = attacker.moves[choice]

    if random.randint(1, 100) <= acc:
        damage = max(1, power + attacker.attack - 40)

        if turn == 0:
            hp2 -= damage
        else:
            hp1 -= damage
        print(f"{attacker.name} used {name}! It hit for {damage} damage.")
    else:
        print(f"{attacker.name} used {name}... MISS!")

    turn = 1 - turn

winner = p1.name if hp1 > 0 else p2.name
print(f"\nBattle Over! {winner} wins!")