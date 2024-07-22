import random

print("Hello World")

# write 'hello world' to the console
# run the script with python app.py
# output: Hello World

user_score = 0

for _ in range(3):
    user_choice = input("Choose between 'rock', 'paper', or 'scissors': ")

    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")

print(f"User score: {user_score}")