import random

from player import Player
from enemies import create_enemies
from combat import fight


def main():
    print("\nWelcome to the Python-RPG")

    name = input("Enter your character's name: ").strip()
    if not name:
        name = "Hero"

    player = Player(name)
    print(f"Welcome, {player.name}!")

    while player.health > 0:
        # Create a fresh enemy list so defeated enemies reset for the next battle.
        enemies = create_enemies()
        enemy = random.choice(list(enemies.values()))

        result = fight(player, enemy)

        if result == "game_over":
            break

        if result == "defeated":
            print("\nYou survived the battle!")
        elif result == "fled":
            print("\nYou live to fight another day.")

        print("\nWhat do you want to do next?")
        print("1. Fight another enemy")
        print("2. Quit")

        choice = input("> ").strip()

        if choice == "2":
            print("\nThanks for playing!")
            break
        elif choice != "1":
            print("Invalid choice. Starting another battle.")


if __name__ == "__main__":
    main()
