import random
import time

round_count = int(input("How many rounds would you like to play? "))
score = 0

for i in range(round_count):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = input("Rock, Paper, Scissors? ").lower()

    if computer_choice == player_choice:
        print("Tie")
        time.sleep(0.5)
        # add_round_for_tie = input("Would you like to add a round because of the tie?")
        # if add_round_for_tie.lower() == "yes":
        # round_count += 1

    else:
        if computer_choice == "paper" and player_choice == "scissors":
            print("Scissors beats paper. You win!")
            score += 1
            time.sleep(0.5)
        if computer_choice == "scissors" and player_choice == "paper":
            print("Scissors beats paper. You lost.")
            time.sleep(0.5)
        if computer_choice == "rock" and player_choice == "scissors":
            print("Rock beats scissors. You lost.")
            time.sleep(0.5)
        if computer_choice == "scissors" and player_choice == "rock":
            print("Rock beats scissors. You win!")
            score += 1
            time.sleep(0.5)
        if computer_choice == "paper" and player_choice == "rock":
            print("Paper beats rock. You lost.")
            time.sleep(0.5)
        if computer_choice == "rock" and player_choice == "paper":
            print("Paper beats rock. You win!")
            score += 1
            time.sleep(0.5)

    if player_choice not in ("rock", "paper", "scissors"):
        print("Invalid input")
        time.sleep(0.5)

print(f"Your score is {score}/{round_count}")
