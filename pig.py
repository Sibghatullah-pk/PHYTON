import random

def roll():
    return random.randint(1, 6)

while True:
    players = input("Enter the number of players (2-6): ")
    if players.isdigit() and 2 <= int(players) <= 6:
        players = int(players)
        break
    else:
        print("Invalid input. Please enter a number between 2 and 6.")

max_score = 50
player_scores = [0] * players
print(f"Starting the game with {players} players. First to reach {max_score} points wins!")
while max(player_scores) < max_score:
    for player in range(players):
        choice = input(f"Player {player + 1}, press Enter to roll the dice or 'q' to quit: ").lower()
        if choice == 'q':
            print("Game ended by player {player+1}.")
            exit

        roll_value = roll()
        if roll_value == 1:
            print(f"Player {player + 1} rolled a 1. Score reset to 0.")
            player_scores[player] = 0
        else:
            print(f"Player {player + 1} rolled a {roll_value}.")
            player_scores[player] += roll_value

        print(f"Player {player + 1}'s total score: {player_scores[player]}")

        # Check if player won
        if player_scores[player] >= max_score:
            print(f" Player {player + 1} wins with {player_scores[player]} points! 🎉")
            exit()

        print("-" * 30)
