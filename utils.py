# utils.py
import time
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_puzzle_state(puzzle, step=None, move=None):
    """Print the puzzle state in a nice format"""
    clear_screen()
    print("\n" + "=" * 20)
    if step is not None and move is not None:
        print(f"Step {step}: Move {move}")
    print("-" * 13)
    for row in puzzle.board:
        print("|", end=" ")
        for num in row:
            if num == 0:
                print(" ", end=" |")
            else:
                print(num, end=" |")
        print("\n" + "-" * 13)
    print("=" * 20 + "\n")

