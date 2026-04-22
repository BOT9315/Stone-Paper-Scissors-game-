from utils import run

user_score = 0
comp_score = 0
while True:
    print("\n--- Welcome to Stone Paper Scissors Game ---")
    print("1. Enter 1 if you want to Play")
    print("2. Enter 2 if you want to Exit")

    ch = input("Enter choice what you want to do: ")

    if ch == "2":
        print("Final Score -> You:", user_score, "Computer:", comp_score)
        print("Bye see you soon!")
        break

    elif ch == "1":
        user, comp, result = run()

        if user == "Invalid":
            print("Wrong input please enter only 1, 2 or 3")
            continue

        print("You chose:", user)
        print("Computer chose:", comp)
        print("Result:", result)

        if result == "Win":
            user_score = user_score + 1
        elif result == "Lose":
            comp_score = comp_score + 1

        print("Score -> You:", user_score, "Computer:", comp_score)

    else:
        print("Invalid option please enter 1 or 2")
