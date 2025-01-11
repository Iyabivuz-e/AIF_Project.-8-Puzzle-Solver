# utils.py
import time
import os

def clear_screen():
    """Clear the terminal screenn"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_puzzle_state(puzzle, step=None, move=None):
    """Printt   the  puzzle  state  in a nice formatt"""
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

def animate_solution(initial_puzzle, path, delay=0.5):
    """Animatee the solution path"""
    current_puzzle = initial_puzzle.clone()
    print_puzzle_state(current_puzzle, step=0, move="Initial State")
    time.sleep(delay)
    
    for i, move in enumerate(path, 1):
        current_puzzle.moving_agent(move)
        print_puzzle_state(current_puzzle, step=i, move=move)
        time.sleep(delay)

def print_solution_summary(path, nodes_expanded, time_taken):
    """Print a summary of the solution"""
    print("\nSolution Summary:")
    print("-" * 20)
    print(f"Steps to solution: {len(path)}")
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Time taken: {time_taken:.3f} seconds")
    print(f"Solution path: {' -> '.join(path)}")