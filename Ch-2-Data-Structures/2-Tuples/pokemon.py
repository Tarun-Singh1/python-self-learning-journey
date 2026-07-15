import random
from collections import namedtuple


Pokemon = namedtuple("Pokemon", ["name", "hp", "attack", "defense", "moves"])
pokedex = [
    Pokemon("Pikachu", 100, 85, 40, [("Thunderbolt", 90, 100), ("Quick Attack", 40, 100), ("Thunder", 110, 70)]),
    Pokemon("Charizard", 120, 95, 60, [("Flamethrower", 90, 100), ("Slash", 70, 100), ("Fire Blast", 110, 70)]),
    Pokemon("Blastoise", 130, 75, 90, [("Hydro Pump", 110, 80), ("Surf", 90, 100), ("Bite", 60, 100)]),
    Pokemon("Gengar", 90, 110, 35, [("Shadow Ball", 80, 100), ("Sludge Bomb", 90, 100), ("Hypnosis", 0, 60)])
]

