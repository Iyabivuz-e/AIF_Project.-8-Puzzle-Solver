##########################################################################################################
#### THE PUZZLE GAME BOILERPLATE : This will help us to move an AI agent in different dirrections  #####
##########################################################################################################

class Puzzle:
    def __init__(self, board):
        self.board = board
        self.size = 3
        self.empty_card = self.find_empty_card()
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost
    
    # A function to find an empty space in the puzzle board
    def find_empty_card(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)

    # A function that moves an agent in differnt directions
    def moving_agent(self, direction):
        x, y = self.empty_card # This shows where the empy row and column is. (x, row; y, column of the empty card)

        if direction == 'up' and x > 0: # Moving upwards
            self.board[x][y], self.board[x-1][y] = self.board[x-1][y], self.board[x][y]
            self.empty_card = (x-1, y) # Updating the empty card after moving
        elif direction == 'down' and x < 2:  # Moving downwards
            self.board[x][y], self.board[x+1][y] = self.board[x+1][y], self.board[x][y]
            self.empty_card = (x+1, y)
        elif direction == 'left' and y > 0:
            self.board[x][y], self.board[x][y-1] = self.board[x][y-1], self.board[x][y]
            self.empty_card = (x, y-1)
        elif direction == 'right' and y < 2:
            self.board[x][y], self.board[x][y+1] = self.board[x][y+1], self.board[x][y] 
            self.empty_card = (x, y+1)

    # Finding the possible movements of the AI agent. If an agent reaches at the top, he cannot move
    def get_possible_moves(self):
        x, y = self.empty_card
        moves = []
        if x > 0 : moves.append('up')
        if x < 2 : moves.append('down')
        if y > 0 : moves.append('left')
        if y < 2 : moves.append('right')
        return moves

    # Function to show the puzzle solved
    def show_the_puzzel(self):
        for row in self.board:
            print(row)
        print("\n")

    def clone(self):
        # Clone the puzzle state manually
        new_board = [row[:] for row in self.board]
        return Puzzle(new_board)

    # Function to see whether is a goal state or not.. It can be used later.
    def is_goal_state(self):
        goal_state = [
            [1,2,3],
            [4,5,6],
            [7,8,0],
        ]
        return self.board == goal_state
