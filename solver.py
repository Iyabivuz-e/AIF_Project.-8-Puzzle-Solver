##########################################################################################################
#### This is the main page that will run the game ##### 
#### If you want to see how it looks and works, you can run this file only. "python solver.py" ##### 
##########################################################################################################

from puzzle import Puzzle
from algorithms import breadth_first_search, depth_first_search, a_star


def main():
    start_board = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    puzzle = Puzzle(start_board)
    print("Initial Puzzle State:")
    puzzle.show_the_puzzel()

    print("Solving with BFS...")
    breadth_first_search(puzzle)

    print("Solving with DFS...")
    depth_first_search(puzzle)

    print("Solving with A* (Manhattan Distance)...")
    a_star(puzzle)


if __name__ == "__main__":
    main()
