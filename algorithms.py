from collections import deque
import time
import heapq
import copy
from utils import board_to_string

################### BREADTH FIRST SEARCH ALGORITHM ########################
def breadth_first_search(puzzle):
    start_time = time.time()
    frontier = deque([puzzle])
    explored = set()
    nodes_explored = 0

    while frontier:
        current_puzzle = frontier.popleft()
        nodes_explored += 1
        print(f"Exploring node {nodes_explored}:")
        current_puzzle.show_the_puzzle()

        if current_puzzle.is_goal_state():
            end_time = time.time()
            print("\nPuzzle is solved with BFS Algorithm!")
            print("Goal state reached!")
            print(f"Time taken: {end_time - start_time:.3f} seconds")
            print("Nodes explored:", nodes_explored)
            return

        explored.add(tuple(map(tuple, current_puzzle.board)))

        for move in current_puzzle.get_possible_moves():
            new_puzzle = current_puzzle.clone()
            new_puzzle.moving_agent(move)
            if tuple(map(tuple, new_puzzle.board)) not in explored:
                frontier.append(new_puzzle)

    print("No solution found.")
    end_time = time.time()
    print("Time taken:", end_time - start_time, "seconds")
    print("Nodes explored:", nodes_explored)


################### DEPTH FIRST SEARCH ALGORITHM ########################
def depth_first_search(puzzle):
    start_time = time.time()
    frontier = deque([puzzle])
    explored = set()
    nodes_explored = 0

    while frontier:
        current_puzzle = frontier.pop()
        nodes_explored += 1
        print(f"Exploring node {nodes_explored}:")
        current_puzzle.show_the_puzzle()

        if current_puzzle.is_goal_state():
            end_time = time.time()
            print("\nPuzzle is solved with DFS Algorithm!")
            print("Goal state reached!")
            print(f"Time taken: {end_time - start_time:.3f} seconds")
            print("Nodes explored:", nodes_explored)
            return

        explored.add(tuple(map(tuple, current_puzzle.board)))

        for move in current_puzzle.get_possible_moves():
            new_puzzle = current_puzzle.clone()
            new_puzzle.moving_agent(move)
            if tuple(map(tuple, new_puzzle.board)) not in explored:
                frontier.append(new_puzzle)

    print("No solution found.")
    end_time = time.time()
    print("Time taken:", end_time - start_time, "seconds")
    print("Nodes explored:", nodes_explored)


################### A* ALGORITHM WITH HEURISTIC MNHATTAN DISTANCE #####################
def heuristic_manhattan(state):
    distance = 0
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)
    }

    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = goal_positions[value]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def a_star(puzzle):

    start_time = time.time()
    nodes_explored = 0
    max_queue_size = 1

    open_set = []
    heapq.heappush(open_set, (0, id(puzzle), puzzle))

    g_scores = {}  # Cost from start to node
    parent_node = {}  # Parent pointers for path reconstruction
    visited = set()  # Set of visited states

    g_scores[puzzle] = 0

    print("\nInitial State:")
    puzzle.show_the_puzzle()

    while open_set:
        max_queue_size = max(max_queue_size, len(open_set))

        current_f, _, current_puzzle = heapq.heappop(open_set)
        nodes_explored += 1

        print(f"\nNodes explored: {nodes_explored}):")
        current_puzzle.show_the_puzzle()

        if current_puzzle.is_goal_state():
            path = []
            current = current_puzzle
            while current in parent_node:
                move, parent = parent_node[current]
                path.append(move)
                current = parent

            path.reverse()

            end_time = time.time()
            time_taken = end_time - start_time

            print("\nPuzzle is solved with A* Algorithm!")

            print("Goal state reached!")
            print(f"Time taken:, {time_taken:.3f}, seconds")
            print("Nodes explored:", nodes_explored)

            return path

        if current_puzzle in visited:
            continue

        visited.add(current_puzzle)

        for move in current_puzzle.get_possible_moves():
            neighbor = current_puzzle.clone()
            neighbor.moving_agent(move)

            if neighbor in visited:
                continue

            tentative_g_score = g_scores[current_puzzle] + 1

            if neighbor not in g_scores:
                g_scores[neighbor] = float('inf')

            if tentative_g_score < g_scores[neighbor]:
                parent_node[neighbor] = (move, current_puzzle)
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + \
                    heuristic_manhattan(neighbor.board)
                neighbor.cost = f_score
                heapq.heappush(open_set, (f_score, id(neighbor), neighbor))

    print("No solution found!")
    return None
