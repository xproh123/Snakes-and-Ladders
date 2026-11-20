import random
import sys
from tabulate import tabulate


snakes = {
    23: 8,
    34: 12,
    43: 17,
    54: 21,
    61: 39,
    73: 45,
    84: 51,
    92: 67
}


ladders = {
    5: 33,
    11: 36,
    14: 63,
    25: 56,
    31: 49,
    40: 78,
    52: 89,
    68: 97
}


rewards = [7, 28, 35, 42, 70, 77, 91]


class Player:
    def __init__(self, name):
        self.name = name # Player's name
        self.position = 0 # Current position
        self.jackpot = 0 # Move to tile 99
        self.items = {
            "twice": False, # Roll twice
            "double": False, # Double the value rolled
            "custom": False # Choose the value of the die
        }
        self.buffs = {
            "advance": False, # Move extra tiles
            "shield": False, # Ignore a snake
            "extra": False # Extra turn
        }


def get_name(i):
    return input(f"Enter player{i}'s name: ")


def dice_roll():
    return random.randint(1,6)


def select_version():
    while True:
        choice = input('Which version do you want to play (1 for Classic, 2 for Plus)? ')
        if choice == "1":
            return "Classic"
        elif choice == "2":
            return "Plus"
        else:
            print('Must type 1 or 2')


def number_of_players():
    while True:
        try:
            number_of_players = int(input('How many players (from 1 to 4): '))
            if 1 <= number_of_players <= 4:
                break
            else:
                print('Number of players must be between 1 to 4')
        except ValueError:
            print('Number of players must be an integer')
    return number_of_players


def give_reward(player, version):
    if version == "Plus" and player.position in rewards:
        print(f"{player.name} landed on a reward tile and obtain a random reward!")
        result = random.randint(1,7)
        if result == 1:
            player.buffs["advance"] = True
            print(f"{player.name} moves forward (1 to 3 tiles)!")
        elif result == 2:
            player.items["twice"] = True
            print(f"{player.name} can roll twice!")
        elif result == 3:
            player.items["double"] = True
            print(f"{player.name} gets a 2x multiplier!")
        elif result == 4:
            player.buffs["shield"] = True
            print(f"{player.name} gets a shield!")
        elif result == 5:
            player.items["custom"] = True
            print(f"{player.name} gets a custom die!")
        elif result == 6:
            player.buffs["extra"] = True
            print(f"{player.name} gets an extra turn!")
        elif result == 7:
            player.jackpot = True
            print(f'{player.name} hits the jackpot and moves to tile 99!')


def select_item(player):
    if any(player.items.values()):
        use_item = input("Do you want to use an item y/n?").lower()
        if use_item == "y":
            while True:
                item_choice = input("Which item do you want to use (1: roll twice, 2: 2x multiplier, 3: custom die): ")
                if item_choice not in ["1", "2", "3"]:
                    continue
                elif item_choice == "1" and player.items["twice"] == False:
                    print("You do not have this item")
                    continue
                elif item_choice == "2" and player.items["double"] == False:
                    print("You do not have this item")
                    continue
                elif item_choice == "3" and player.items["custom"] == False:
                    print("You do not have this item")
                    continue
                else:
                    return item_choice                


def snakes_or_ladders(player, version):
    if player.position in snakes:
        print(f"{player.name} landed on a snake!")
        if version == 'Plus' and player.buffs["shield"] == True:
            player.buffs["shield"] = False
            print('Shield lost.')
        else:
            player.position = snakes[player.position]
    if player.position in ladders:
        print(f"{player.name} landed on a ladder!")
        player.position = ladders[player.position]


def main():

    # Welcome
    print('Welcome to Snakes and Ladders!')

    # Visualize the game board
    game_board = []
    for i in range(10, 0, -1):
        if i % 2 == 0:
            row = list(range(i * 10, i * 10 - 10, -1))
        else:
            row = list(range(i * 10 - 9, i * 10 + 1, 1))
        game_board.append(row)
    print(tabulate(game_board, tablefmt="grid"))

    # Create player list
    player_list = [Player(get_name(i + 1)) for i in range(number_of_players())]
    player_index = 0
    
    # Select game version
    version = select_version()
    print(f'Snakes and Ladders {version} starts!'.replace("Classic ", ""))

    # Main game loop
    while True:
        current_player = player_list[player_index]
        item_select = 0

        print(f"{current_player.name}'s turn")


        # Item using prompt
        item_select = select_item(current_player)

        # Die rolling prompt
        while True:
            action = input(f'{current_player.name}, press E to roll the die: ').lower()
            if action == "e":
                break
        
        # Items in effect
        if version == 'Plus' and item_select == "1":
            steps = dice_roll() + dice_roll()
            current_player.items["twice"] = False
            item_select = 0
        elif version == 'Plus' and item_select == "2":
            steps = dice_roll()*2
            current_player.items["double"] = False
            item_select = 0
        elif version == 'Plus' and item_select == "3":
            while True:
                try:
                    selection = int(input("Choose die's value (from 1 to 6): "))
                    if selection in [1, 2, 3, 4, 5, 6]:
                        steps = selection
                        current_player.items["custom"] = False
                        item_select = 0
                        break
                    print('Must type an integer from 1 to 6')
                except ValueError:
                    print('Must type an integer from 1 to 6')

        # If no items involved
        else:
            steps = dice_roll()
        print(f'{current_player.name} rolled a {steps}')
        
        # Move player if possible
        if current_player.position + steps <= 100:
            current_player.position += steps

        # If landed on a snake or ladder 
        snakes_or_ladders(current_player, version)

        # If landed on a reward tile
        give_reward(current_player, version)

        if version == "Plus" and current_player.buffs["advance"] == True:
            extra_tiles = random.randint(1,3)
            print(f"{current_player.name} moves {extra_tiles} more tiles!")
            current_player.position += extra_tiles
            current_player.buffs["advance"] = False

        # If the jackpot is hit
        if version == 'Plus' and current_player.jackpot == True:
            current_player.position = 99
            current_player.jackpot = False

        # Print current position
        for player in player_list:
            print(f"{player.name} is at: {player.position}")
        
        # Win condition
        if current_player.position == 100:
            print(f'{current_player.name} wins!')
            break

        # Get an extra turn if rolled a 6
        if steps == 6:
            print(f'{current_player.name} rolled a 6 and get an extra turn!')
            continue
        elif version == "Plus" and current_player.buffs["extra"] == True:
            current_player.buffs["extra"] = False
            continue
        else:
            player_index = (player_index + 1) % len(player_list)

    # Ask for another game
    while True:
        again = input('Another game y/n? ').lower()
        if again != 'y':
            print('See you next time :)')
            sys.exit()
        main()

if __name__ == "__main__":
    main()