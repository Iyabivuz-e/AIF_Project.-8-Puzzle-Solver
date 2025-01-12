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
    puzzle.show_the_puzzle()
    
    print("# Solving with BFS Algo #\n")
    breadth_first_search(puzzle)

    print("\n# Solving with DFS #\n")
    depth_first_search(puzzle)

    print("\n# Solving with A* (Manhattan Distance) #\n")
    a_star(puzzle)


if __name__ == "__main__":
    main()
