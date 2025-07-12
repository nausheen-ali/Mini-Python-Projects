import random

def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
    }

    roll=input("Roll the dice? (Y/N):")
    while roll.lower()=="y":
        try:
            num=int(input("Enter no. of dice:"))
            if num<=0:
                print("Must have atleast one dice to roll.")
                continue
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        result=[random.randint(1,6) for _ in range(num)]
        print("Dice rolled:", result)

        for i in range(5):
            line=" ".join(dice_drawing[d][i] for d in result)
            print(line)

        roll=input("Roll again? (Y/N):")

roll_dice()