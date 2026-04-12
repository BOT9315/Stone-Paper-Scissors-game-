import random

def user_choice():
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")

    n = input("Enter number: ")

    if n == "1":
        return "Stone"
    elif n == "2":
        return "Paper"
    elif n == "3":
        return "Scissors"
    else:
        print("Invalid input") 
        return "Invalid"


def computer_choice():
    data = ["Stone", "Paper", "Scissors"]
    c = random.choice(data)
    return c