import random

def easy_level(board):
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available_moves)