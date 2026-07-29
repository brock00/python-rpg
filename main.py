import random       #this is a test commit
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

#print("\nKeep Exploring?")
#print("1. Yes")
#print("2. No")
#choice = input("> ")

#if choice == "1":
 #   fight(player, enemy)
#elif choice == "2":
  #  print("Goodbye!")