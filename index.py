from puzzle import Puzzle
from algorithms import breadth_first_search, depth_first_search
from utils import animate_solution, print_solution_summary

def main():
    # Example initial state (you can modify this)
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
    
    puzzle = Puzzle(initial_state)
    
    print("Initial State:")
    puzzle.show_the_puzzle()
    
    print("\nSolving with BFS...")
    path, nodes, time = breadth_first_search(puzzle)
    
    if path:
        print("\nSolution found!")
        animate_solution(puzzle, path)
        print_solution_summary(path, nodes, time)
    else:
        print("\nNo solution found!")
    
    # Test DFS as well
    print("\nSolving with DFS...")
    path, nodes, time = depth_first_search(puzzle)
    
    if path:
        print("\nSolution found!")
        animate_solution(puzzle, path)
        print_solution_summary(path, nodes, time)
    else:
        print("\nNo solution found!")

if __name__ == "__main__":
    main()