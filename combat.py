def fight(player, enemy):
    print(f"\nA {enemy.name} appeared!")
   
    while player.health > 0 and enemy.health > 0:

        print("\nWhat do you want to do?")
        print("1. Attack")
        print("2. Flee")

        choice = input("> ")

        if choice == "1":
# Player attack
            damage = player.attack - enemy.defense
            damage = max(1, damage)

            enemy.health -= damage

            print(f"\n{player.name} attacks {enemy.name} for {damage} damage!")
            print(f"{enemy.name} HP: {enemy.health}")

            if enemy.health <= 0:
                print(f"{enemy.name} was defeated!")

                print("\nKeep Exploring?")
                print("1. Yes")
                print("2. No")
                choice = input("> ")

                if choice == "1":
                    fight(player, enemy)
                elif choice == "2":
                    print(f"Farewell + {player.name}!")
                    break
            

# Enemy Attack
            damage = enemy.attack - player.defense
            damage = max(1, damage)

            player.health -= damage

            print(f"{enemy.name} attacks {player.name} for {damage} damage!")
            print(f"{player.name} HP: {player.health}")

            if player.health <= 0:
                print(f"{player.name} was defeated! Game Over!")
# Flee
        elif choice == "2":
            print(f"{player.name} escaped!")
            break

        else:
            print("Invalid choice!")