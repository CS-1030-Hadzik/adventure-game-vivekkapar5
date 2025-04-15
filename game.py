import sys

class Player:
    def __init__(self):
        self.inventory = []
        self.health = 100

def explore_dark_woods(player):
    print("\nYou explore the dark woods and find a lantern!")
    if "lantern" not in player.inventory:
        player.inventory.append("lantern")
    print(f"Health: {player.health}")

def explore_mountain_pass(player):
    print("\nYou cross the mountain pass and find a map!")
    if "map" not in player.inventory:
        player.inventory.append("map")
    print(f"Health: {player.health}")

def explore_cave(player):
    print("\nYou approach the dark cave...")
    if "lantern" in player.inventory:
        print("With the lantern, you safely explore and find a treasure!")
        if "treasure" not in player.inventory:
            player.inventory.append("treasure")
    else:
        print("It's too dark! You trip and hurt yourself.")
        player.health -= 10
    print(f"Health: {player.health}")

def explore_hidden_valley(player):
    print("\nYou enter the hidden valley...")
    if "map" in player.inventory:
        print("Using the map, you find some rare herbs!")
        if "rare herbs" not in player.inventory:
            player.inventory.append("rare herbs")
    else:
        print("You get lost and exhausted without a map.")
        player.health -= 10
    print(f"Health: {player.health}")

def stay_still(player):
    print("\nYou stay still, doing nothing... but lose energy.")
    player.health -= 10
    print(f"Health: {player.health}")

def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print("\n🎉 Congratulations! You found both the treasure and the rare herbs. You win!")
        sys.exit()

def check_lose(player):
    if player.health <= 0:
        print("\n💀 Your health dropped to zero. Game Over.")
        sys.exit()

def main():
    player = Player()
    print("🏞️ Welcome to the Final Adventure Game!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Explore the dark woods")
        print("2. Cross the mountain pass")
        print("3. Explore the cave")
        print("4. Explore the hidden valley")
        print("5. Stay still")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            explore_dark_woods(player)
        elif choice == "2":
            explore_mountain_pass(player)
        elif choice == "3":
            explore_cave(player)
        elif choice == "4":
            explore_hidden_valley(player)
        elif choice == "5":
            stay_still(player)
        else:
            print("Invalid choice. Try again.")

        check_win(player)
        check_lose(player)

# Start the game
main()
