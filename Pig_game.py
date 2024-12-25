import random
import time

# Emoji representations
dice_emojis = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
win_emoji = "🏆"
game_over_emoji = "❌"

print("Welcome to the PIG Game!!!")
num_players = int(input("How many human players are playing? "))  # Number of human players

# Ask for player names
player_names = []
for i in range(num_players):
    name = input(f"Enter name for Player {i + 1}: ")
    player_names.append(name)

# Add Computer player
player_names.append("Computer")

print("The rules of the game are:")
print("1. You will get to roll a dice once.")
print("2. If the number is other than one, then the number will be added to your score.")
print("3. If the number is one, then your score becomes zero and it's the next player's turn.")
print("4. Whoever reaches 40 points first or more wins.")
time.sleep(5)
print("Let's play the game!!!!!\n")

# Initialize scores for each player
player_scores = [0] * (num_players + 1)  # Additional slot for the computer player

# Target score
target_score = 40

# Main game loop
current_player = 0
while True:
    print(f"\n{player_names[current_player]}'s turn:")
    
    # Check if the current player is human or computer
    if current_player < num_players:
        is_human = True
    else:
        is_human = False
    
    if is_human:
        while True:
            dice = random.randint(1, 6)
            if dice == 1:
                print("You rolled a 1!!! Your score becomes zero ", game_over_emoji)
                player_scores[current_player] = 0
                break
            else:
                print("You rolled:", dice_emojis[dice - 1])
                player_scores[current_player] += dice
                print("Your current score is", player_scores[current_player])

            if player_scores[current_player] >= target_score:
                print(f"Congratulations, {player_names[current_player]}! You reached {target_score} points or more and won the game!", win_emoji)
                exit()

            ask = input("Do you want to continue? (yes/no): ").lower()
            if ask != "yes":
                print(f"{player_names[current_player]} chose not to continue. Current score saved.")
                break
    else:  # Computer player
        rolls_left = 3
        while rolls_left > 0:
            dice = random.randint(1, 6)
            if dice == 1:
                print("Computer rolled a 1!!! Its score becomes zero ", game_over_emoji)
                player_scores[current_player] = 0
                break
            else:
                print("Computer rolled:", dice_emojis[dice - 1])
                player_scores[current_player] += dice
                print("Computer's current score is", player_scores[current_player])
            rolls_left -= 1

    current_player = (current_player + 1) % (num_players + 1)

    # Print scores table with emojis
    print("\nScores Table:")
    print("-" * 30)
    for i in range(num_players + 1):
        print(f"{player_names[i]}: {player_scores[i]}")
    print("-" * 30)
