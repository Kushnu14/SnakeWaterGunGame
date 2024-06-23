import random

while True:
    play = input("Enter 'p' to play and 'e' to exit : ").strip().lower()

    if play == "e":
        print("Exiting the game. Goodbye!")
        exit()  # Exit the program immediately

    else:
       computer = random.choice([-1, 0, 1])
       youstr = input("Enter 's' for Snake, 'w' for Water, 'g' for Gun: ").strip().lower()
       

       youDict = {
            "s": 1,
            "w": -1,
            "g": 0
        }
       reverseDict = {
            1: "Snake", -1: "Water", 0: "Gun"
        }
       you = youDict[youstr]
       print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

       if computer == you:
            print("It's a draw!")
       else:
            if (computer == 1 and you == -1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
                print("You Lose!")
            elif (computer == 0 and you == 1) or (computer == -1 and you == 0) or (computer == -1 and you == 1):
                print("You Win!")


    