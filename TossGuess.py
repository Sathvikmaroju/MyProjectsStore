# GUESS THE TOSS (H-0, T-1)
import random

count_zero, count_one, player_score, computer_score = 0, 0, 0, 0

def prediction():
    if count_zero > count_one: predict = 0
    elif count_zero < count_one: predict = 1
    else: predict = random.randint(0, 1)
    return predict

def update_counts(player_input):
    global count_zero, count_one
    if player_input == 0: count_zero += 1
    else: count_one += 1

def update_scores(predicted, player_input):
    global player_score, computer_score
    if predicted == player_input:
        computer_score = computer_score + 1
        print("Computer Score:", computer_score,"\nPlayer Score:", player_score)
    else:
        player_score = player_score + 1
        print("Computer Score:", computer_score,"\nPlayer Score:", player_score)

def game_play():
    valid_entries = ['1', '0']
    target=int(input("Enter Target: "))
    while True:
        global player_score, computer_score
        predicted = prediction()
        player_input = input("Enter either 0 or 1: ")
        while player_input not in valid_entries:
            player_input = input("Invalid Input!\nPlease enter either 0 or 1: ")

        player_input = int(player_input)
        update_counts(player_input)
        update_scores(predicted, player_input)

        if player_score == target:
            print("Congrats, You Won!")
            break
        elif computer_score == target:
            print("Bad Luck, You Lost!")
            break

game_play()