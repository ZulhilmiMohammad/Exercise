import random

# Define player and enemy classes
class Lion:
    def __init__(self, name, health, damage,roar):
        self.name = name
        self.health = health
        self.damage = damage
        self.roar = roar 

class Werewolf:
    def __init__(self, name, health, damage,roar):
        self.name = name
        self.health = health
        self.damage = damage
        self.roar = roar

# Define the game loop
def game_loop():
    # Create the player and enemy
    lion = Lion("Simba", 100, 20 , "meowww")
    werewolf = Werewolf("Roger", 100, 20 , "wooff wooff")

    print("Animals ready to fight...")

    # Game loop
    while True:
        print(f"\n{lion.name} has {lion.health} health left.")
        print(f"{werewolf.name} has {werewolf.health} health left.")

        # Player turn
        lion_choice = random.choice(["a", "h"])
        if lion_choice == "a":
            werewolf.health -= lion.damage
            print(f"{lion.name} {lion.roar} before attack")
            print(f"{lion.name} attack {werewolf.name} for {lion.damage} damage!")
        elif lion_choice == "h":
            lion.health += 10
            print(f"{lion.name} heals himself for 10 health points!")

        # Check if enemy is defeated
        if werewolf.health <= 0:
            print(f"\n{werewolf.name} has been defeated by {lion.name}!")
            break

        # Enemy turn
        werewolf_choice = random.choice(["a", "h"])
        if werewolf_choice == "a":
            lion.health -= werewolf.damage
            print(f"{werewolf.name} {werewolf.roar} before attack")
            print(f"{werewolf.name} attacks {lion.name} for {werewolf.damage} damage!")
        elif werewolf_choice == "h":
            werewolf.health += 10
            print(f"{werewolf.name} heals himself for 10 health points!")

        # Check if player is defeated
        if lion.health <= 0:
            print(f"\n{lion.name} has been defeated by {werewolf.name}!")
            break

# Call the game loop
game_loop()
