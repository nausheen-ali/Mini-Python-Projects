import random

exit_game = False
user_points = 0
computer_points = 0

options = {1: "rock", 2: "paper", 3: "scissors"}

while not exit_game:
    print("\n--- Rock Paper Scissors ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("0. Exit")

    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number only!")
        continue

    if user_choice == 0:
        print("\nGame ended")
        print(f"You: {user_points} | Computer: {computer_points}")
        exit_game = True
        break

    if user_choice not in options:
        print("Invalid choice! Choose 1, 2, or 3.")
        continue

    user_input = options[user_choice]
    computer_input = random.choice(list(options.values()))

    print(f"\nYour input: {user_input}")
    print(f"Computer input: {computer_input}")

    if user_input == computer_input:
        print("It's a tie!")
    elif (
        (user_input == "rock" and computer_input == "scissors") or
        (user_input == "paper" and computer_input == "rock") or
        (user_input == "scissors" and computer_input == "paper")
    ):
        print("You win!")
        user_points += 1
    else:
        print("Computer wins!")
        computer_points += 1
