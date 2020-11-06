import random

count_rock, count_paper, count_scissors = 0, 0, 0

def update_counts(user_input):
    global count_rock, count_paper, count_scissors
    if user_input == 0: count_rock += 1
    elif user_input == 1: count_paper += 1
    elif user_input == 2: count_scissors += 1

def predict():
    if count_rock > count_paper and count_rock > count_scissors: return 0
    elif count_paper > count_rock and count_paper > count_scissors: return 1
    elif count_scissors > count_rock and count_scissors > count_paper: return 2
    else: return random.randint(0, 2)

player_score, comp_score = 0, 0

def update_scores(user_input):
    global player_score, comp_score
    pred = predict()
    if user_input == 0:
        if pred == 0:
            print("\nYou played ROCK, computer played ROCK.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")
        elif pred == 1:
            comp_score += 1
            print("\nYou played ROCK, computer played PAPER.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")
        else:
            player_score += 1
            print("\nYou played ROCK, computer played SCISSORS.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")
    elif user_input == 1:
        if pred == 0:
            player_score += 1
            print("\nYou played PAPER, computer played ROCK.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")
        elif pred == 1:
            print("\nYou played PAPER, computer played PAPER.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")
        else:
            comp_score += 1
            print("\nYou played PAPER, computer played SCISSORS.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")
    elif user_input == 2:
        if pred == 0:
            comp_score += 1
            print("\nYou played SCISSORS, computer played ROCK.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")
        elif pred == 1:
            player_score += 1
            print("\nYou played SCISSORS, computer played PAPER.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")
        else:
            print("\nYou played SCISSORS, computer played SCISSORS.\nComputer Score: ", comp_score, "\nYour Score: ", player_score,"\n")

def gamePlay():
    valid_entries = [0, 1, 2]
    target = int(input("Enter Target: "))
    while True:
        user_input = int(input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: "))
        while user_input not in valid_entries:
            print("Invalid Input!")
            user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")
        update_scores(user_input)
        update_counts(user_input)
        if comp_score == target:
            print("Computer Won!")
            break
        elif player_score == target:
            print("You won!")
            break

gamePlay()