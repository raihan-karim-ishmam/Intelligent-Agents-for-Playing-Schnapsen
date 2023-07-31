import random

class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        moves = state.moves()

        random.shuffle(moves)

        cheapest = moves[0]

        for move in moves:
            if cheapest[0] % 5 <= move[0] % 5:
                cheapest = move

        return cheapest