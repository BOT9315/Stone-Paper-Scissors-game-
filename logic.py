def check(user, comp):
    if user == comp:
        return "Draw"

    if user == "Stone" and comp == "Scissors":
        return "Win"

    if user == "Paper" and comp == "Stone":
        return "Win"

    if user == "Scissors" and comp == "Paper":
        return "Win"

    return "Lose"