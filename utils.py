from choice import user_choice, computer_choice
from logic import check

def run():
    user = user_choice()
    comp = computer_choice()
    result = check(user, comp)
    return user, comp, result