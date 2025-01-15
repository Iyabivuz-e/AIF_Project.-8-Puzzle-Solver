import copy

class Puzzle:
    def __init__(self, board):
        self.board = board
        self.size = 3
        self.empty_card = self.find_empty_card()
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost

    def find_empty_card(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)

    def moving_agent(self, direction):
        x, y = self.empty_card

        if direction == 'up' and x > 0:
            self.board[x][y], self.board[x -
                                         1][y] = self.board[x-1][y], self.board[x][y]
            self.empty_card = (x-1, y)
        elif direction == 'down' and x < 2:
            self.board[x][y], self.board[x +
                                         1][y] = self.board[x+1][y], self.board[x][y]
            self.empty_card = (x+1, y)
        elif direction == 'left' and y > 0:
            self.board[x][y], self.board[x][y -
                                            1] = self.board[x][y-1], self.board[x][y]
            self.empty_card = (x, y-1)
        elif direction == 'right' and y < 2:
            self.board[x][y], self.board[x][y +
                                            1] = self.board[x][y+1], self.board[x][y]
            self.empty_card = (x, y+1)

    def get_possible_moves(self):
        x, y = self.empty_card
        moves = []
        if x > 0:
            moves.append('up')
        if x < 2:
            moves.append('down')
        if y > 0:
            moves.append('left')
        if y < 2:
            moves.append('right')
        return moves

    def show_the_puzzle(self):
        for row in self.board:
            print(row)
        print(" ")

    def clone(self):

        return copy.deepcopy(self)

    def is_goal_state(self):
        goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0],
        ]

        return self.board == goal_state
