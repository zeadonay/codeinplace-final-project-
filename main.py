import random


def print_map(player, treasure, key, has_key, traps, coin_locations, heart_locations, visited):
    print("\n--- MAP ---")

    print("  ", end="")
    for col in range(7):
        print(col, end=" ")
    print()

    for row in range(7):
        print(row, end=" ")

        for col in range(7):
            cell = [row, col]

            if cell == player:
                print("P", end=" ")
            elif cell == treasure:
                print("T", end=" ")
            elif cell not in visited:
                print("?", end=" ")
            elif cell == key and not has_key:
                print("K", end=" ")
            elif cell in traps:
                print("!", end=" ")
            elif cell in coin_locations:
                print("$", end=" ")
            elif cell in heart_locations:
                print("+", end=" ")
            else:
                print(".", end=" ")

        print()

    print("--- END MAP ---")
    print("P=you  T=treasure  K=key  !=trap  $=coins  +=life  ?=unknown")


print("PIRATE TREASURE QUEST")
name = input("What is your pirate name? ")
print(f"""
Welcome, Captain {name}!
For hundreds of years, sailors have searched for the
legendary treasure, One Piece. It was hidden by the Pirate
King, Captain Gol D. Roger.

After a long and dangerous journey across the seas, you have
finally discovered the island where the treasure is buried.
But the treasure chest is locked, and only the Golden Key
can open it.

Explore the island, collect coins, earn extra lives, avoid
deadly traps, and overcome challenging obstacles. Find the
Golden Key, unlock the treasure, and become the next Pirate King!

Good luck, Captain {name}!
""")

size = 7
player = [0, 0]
treasure = [6, 6]
lives = 3
coins = 0
has_key = False
won = False

visited = []
visited.append([0, 0])

key = [random.randint(1, 5), random.randint(1, 5)]

traps = []
while len(traps) < 6:
    trap = [random.randint(0, 6), random.randint(0, 6)]
    if trap != player and trap != treasure and trap != key and trap not in traps:
        traps.append(trap)

coin_locations = []
while len(coin_locations) < 6:
    coin = [random.randint(0, 6), random.randint(0, 6)]
    if (
        coin != player
        and coin != treasure
        and coin != key
        and coin not in traps
        and coin not in coin_locations
    ):
        coin_locations.append(coin)

heart_locations = []
while len(heart_locations) < 2:
    heart = [random.randint(0, 6), random.randint(0, 6)]
    if (
        heart != player
        and heart != treasure
        and heart != key
        and heart not in traps
        and heart not in coin_locations
        and heart not in heart_locations
    ):
        heart_locations.append(heart)

while lives > 0:

    print_map(player, treasure, key, has_key, traps, coin_locations, heart_locations, visited)

    print("\n" + "=" * 30)
    print(f"Location : row {player[0]}, col {player[1]}")
    print(f"Lives    : {lives}")
    print(f"Coins    : {coins}")
    print(f"Key      : {'Yes' if has_key else 'No'}")
    print("=" * 30)

    if coins >= 30 and lives < 5:
        buy = input("Buy an extra life for 30 coins? (y/n): ").lower()
        if buy == "y":
            coins -= 30
            lives += 1
            print("You bought an extra life!")

    move = input("Move (w=up, s=down, a=left, d=right): ").lower()

    if move == "w" and player[0] > 0:
        player[0] -= 1
    elif move == "s" and player[0] < size - 1:
        player[0] += 1
    elif move == "a" and player[1] > 0:
        player[1] -= 1
    elif move == "d" and player[1] < size - 1:
        player[1] += 1
    else:
        print("Invalid move! Use w, a, s, or d.")
        continue

    if player not in visited:
        visited.append(player.copy())

    if player in traps:
        lives -= 1
        print("\nBOOM! You stepped on a trap!")
        print("You were sent back to the beach.")
        player = [0, 0]
        if [0, 0] not in visited:
            visited.append([0, 0])

    else:
        if player == key and not has_key:
            has_key = True
            print("\nYou found the Golden Key!")

        if player in coin_locations:
            coins += 10
            coin_locations.remove(player)
            print("\nYou found 10 gold coins!")

        if player in heart_locations:
            lives += 1
            heart_locations.remove(player)
            print("\nLucky day! You found an extra life!")

        if player == treasure:
            if has_key:
                print_map(player, treasure, key, has_key, traps, coin_locations, heart_locations, visited)
                print("\n*** TREASURE FOUND! ***")
                print(f"Congratulations, Captain {name}!")
                print(f"You escaped with {coins} gold coins.")
                print("YOU WIN!")
                won = True
                break
            else:
                print("\nThe treasure chest is locked!")
                print("Find the Golden Key first.")

if not won:
    print("\nGAME OVER")
    print("The island has claimed another pirate...")
