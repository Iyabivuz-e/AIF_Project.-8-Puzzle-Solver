# Helper function: Converts the board into a string for easy comparison
def board_to_string(board):
    return ''.join(str(cell) for row in board for cell in row)
