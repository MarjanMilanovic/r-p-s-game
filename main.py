import random


def main():
    cp_score = 0
    player_score = 0
    win_score = 3
    print(f"Hello there, Mike would like to play a game. You are playing first to {win_score} .")

    while player_score != win_score and cp_score != win_score:
        player_choice = input("Rock, Paper, or Scissors? ")
        choices = ["Rock", "Paper", "Scissors"]
        cp_choice = choices[random.randint(0, 2)]

        if player_choice == "Rock":
            if cp_choice == "Rock":
                print(f"We have a tie. Play again.\nThe score is CP {cp_score}:{player_score} You.")
            elif cp_choice == "Paper":
                cp_score += 1
                print(f"CP wins with {cp_choice}.\nThe score is CP {cp_score}:{player_score} You.")
            elif cp_choice == "Scissors":
                player_score += 1
                print(f"You win against {cp_choice}.\nThe score is CP {cp_score}:{player_score} You.")

        elif player_choice == "Paper":
            if cp_choice == "Paper":
                print(f"We have a tie. Play again.\nThe score is CP {cp_score}:{player_score} You.")
            elif cp_choice == "Scissors":
                cp_score += 1
                print(f"CP wins with {cp_choice}.\nThe score is CP {cp_score}:{player_score} You.")
            elif cp_choice == "Rock":
                player_score += 1
                print(f"You win against {cp_choice}.\nThe score is CP {cp_score}:{player_score} You.")

        elif player_choice == "Scissors":
            if cp_choice == "Scissors":
                print(f"We have a tie. Play again.\nThe score is CP {cp_score}:{player_score} You.")
            elif cp_choice == "Rock":
                cp_score += 1
                print(f"CP wins with {cp_choice}.\nThe score is CP {cp_score}:{player_score} You.")
            elif cp_choice == "Paper":
                player_score += 1
                print(f"You win against {cp_choice}.\nThe score is CP {cp_score}:{player_score} You.")
        elif player_choice not in choices:
            print("Please use a valid phrase.")

    else:
        if player_score == win_score:
            print("YOU WIN!")

        elif cp_score == win_score:
            print("CP WINS!")


main()
