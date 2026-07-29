import random       
from player import Player
from enemies import create_enemies
from combat import fight

print("\nWelcome to the Python-RPG")

name = input("Enter your character's name: ")

player = Player(name)

print(f"Welcome, {player.name}!")

enemies = create_enemies()

enemy = random.choice(list(enemies.values()))

fight(player, enemy)
