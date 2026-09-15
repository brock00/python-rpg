import random

from enemies import create_enemies


def fight(player, enemy):
    print(f"\nA {enemy.name} appeared!")

    while player.health > 0:
        print("\nWhat do you want to do?")
        print("1. Attack")
        print("2. Flee")

        choice = input("> ")

        if choice == "1":
            damage = max(1, player.attack - enemy.defense)
            enemy.health -= damage

            print(f"\n{player.name} attacks {enemy.name} for {damage} damage!")
            print(f"{enemy.name} HP: {max(0, enemy.health)}")

            if enemy.health <= 0:
                print(f"{enemy.name} was defeated!")
                print("\nKeep Exploring?")
                print("1. Yes")
                print("2. No")
                choice = input("> ")

                if choice == "1":
                    # A new object ensures the next enemy begins at full health.
                    enemy = random.choice(list(create_enemies().values()))
                    print(f"\nA {enemy.name} appeared!")
                    continue
                if choice == "2":
                    print(f"Farewell {player.name}!")
                    break

                print("Invalid Option!")
                continue

            damage = max(1, enemy.attack - player.defense)
            player.health -= damage

            print(f"{enemy.name} attacks {player.name} for {damage} damage!")
            print(f"{player.name} HP: {max(0, player.health)}")

            if player.health <= 0:
                print(f"{player.name} was defeated! Game Over!")
                break

        elif choice == "2":
            print(f"{player.name} Escaped!")
            break

        else:
            print("Invalid choice!")

