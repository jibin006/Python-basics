import random

options = ["rock","paper","scissors"]

user_score = 0
computer_score = 0

while True:
    user_input = input ("Type rock or paper or scissors or q for quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("invalid")
        continue

    computer_input = random.choice(options)
    print("computer choose", computer_input)

    if (user_input == "rock" and computer_input == "scissors") or \
       (user_input == "paper" and computer_input == "rock") or \
       (user_input == "scissors" and computer_input == "paper"):
       print("you won!")
       user_score += 1
    elif (user_input) == (computer_input):
        print("its tie!") 

    else:
        print("you loss")   

    print("you got", user_score,  "in total")       
