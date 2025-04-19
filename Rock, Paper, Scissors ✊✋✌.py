import random

choices = ["rock", "paper", "scissors"]

print("Rock, Paper, Scissors Game ✊✋✌")

rounds = input("How many rounds do you want to play? ")

# Validate that input is a number
while not rounds.isdigit():
    rounds = input("Please enter a valid number of rounds: ")

rounds = int(rounds)
wins = 0
losses = 0
ties = 0

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    user = input("Choose rock, paper or scissors: ").lower()

    while user not in choices:
        print("Invalid choice. Try again!")
        user = input("Choose rock, paper or scissors: ").lower()

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
        ties += 1
    elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

# Final results
print("\nGame Over!")
print(f"Total Rounds: {rounds}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Ties: {ties}")


