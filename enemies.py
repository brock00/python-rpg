from enemy import Enemy

def create_enemies():
    return {
        "Goblin": Enemy("Goblin", 40, 8, 3),
        "Wolf": Enemy("Wolf", 30, 10, 2),
        "Dragon": Enemy("Dragon", 300, 35, 20)
    }