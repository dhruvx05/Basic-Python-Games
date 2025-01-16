import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

players = int(input("Enter number of players (2-4): "))
if players < 2 or players > 4:
    print("Invalid number of players. Must be between 2 to 4.")
    exit()

max_score = 20
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has started!\n")
        print("Your total score is:", player_scores[player_index])
        current_score = 0

        should_roll = input("Would you like to roll (y)? ")
        if should_roll.lower() == "y":
            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done")
            else:
                current_score += value
                print("You rolled a:", value, "!")
            
            print("Your score is:", current_score)

        player_scores[player_index] += current_score

        print("Your total score is:", player_scores[player_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number", winning_index + 1, "is the winner with the score of:", max_score)
