import random

class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        moves = state.moves()

        random.shuffle(moves)

        expensive = moves[0]

        for move in moves:
            if expensive[0] % 5 >= move[0] % 5:
                expensive = move

        return expensive