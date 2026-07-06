"""Supports a round of rock, paper, scissors between a user and a computer."""

import random

def make_user_choice():
    """Returns the user's choice of rock, paper, or scissors."""
    user_decision = str(input("Choose one: rock, paper, scissors? "))
    while user_decision != "rock" and user_decision != "paper" and user_decision != "scissors":
        user_decision = input("Pick one of them: rock, paper, or scissors")
    return user_decision
def make_computer_choice():
    """Returns the computer's random choice of rock, paper, or scissors."""
    played_number = random.randint(1,3)
    if played_number == 1:
        return "scissors"
    elif played_number == 2:
        return "rock"
    else:
        return "paper"
    
def wins_matchup(choice, opponent_choice):
    """Returns True if the first player's choice wins over their opponent.

    Choices can be rock, paper, or scissors. Assumes the choices are different.
    """
    if choice == "rock":
        return opponent_choice != "paper"
    #if I pick rock and the computer picks paper, it is false. 
    elif choice == "paper":
        return opponent_choice != "scissors"
    elif choice == "scissors":
        return opponent_choice != "rock"

def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    return ">> Score: " + str(user_score) + "-" + str(computer_score)
