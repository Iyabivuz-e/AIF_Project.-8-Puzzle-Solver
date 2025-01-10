##################################################################################################
#### OMRAN: TODO: Implement bfs and dfs algorithms based on the puzzle.py boilerplate   #####
##################################################################################################
import heapq  
import heapq
import copy
from utils import board_to_string


def breadth_first_search(puzzle):
    # queue = [puzzle]
    # visited = set()
    pass


def depth_first_search(puzzle):
    pass


def a_star(puzzle):
    # Priority queue to store states to explore
    priority_queue = []

    # Start state is the initial puzzle configuration
    start_state = puzzle
    start_state.g_cost = 0  # Cost from the start to this state
    start_state.h_cost = heuristic_manhattan(
        start_state.board)  # Estimated cost to goal
    start_state.f_cost = start_state.g_cost + start_state.h_cost  # Total cost

    # Keep track of visited states and the cost to reach them
    initial_board_state = board_to_string(start_state.board)
    visited = {initial_board_state: 0}
    came_from = {initial_board_state: None}

    # Add the start state to the queue
    heapq.heappush(priority_queue, (start_state.f_cost, 0, start_state))
    print(f"Start state added to the queue with f_cost: {start_state.f_cost}")

    moves_count = 0  # To count the number of moves made

    # Main loop: Process the queue until it's empty
    while priority_queue:
        print("\nQueue size:", len(priority_queue))
        current_f_cost, _, current_state = heapq.heappop(priority_queue)
        current_board_str = board_to_string(current_state.board)
        print(f"Exploring state with f_cost: {current_f_cost}")

        # Skip this state if a better cost is already recorded
        if current_board_str in visited and visited[current_board_str] < current_state.g_cost:
            print("Skipping state as it was already visited with a lower cost")
            continue

        # Display the current state
        print("Current puzzle state:")
        current_state.show_the_puzzel()

        # Check if the goal is reached
        if current_state.is_goal_state():
            print("\nPUZZLE SOLVED!")
            print(f"Solution found in {moves_count} moves")
            return current_state

        # Explore possible moves from the current state
        print("Exploring possible moves...")
        for move in current_state.get_possible_moves():
            new_state = current_state.clone()  # Create a new state
            new_state.moving_agent(move)  # Apply the move

            new_g_cost = current_state.g_cost + 1  # Increment g_cost
            new_board_str = board_to_string(
                new_state.board)  # Get new state as a string

            # Skip if the new state has already been visited with a lower cost
            if new_board_str in visited and visited[new_board_str] <= new_g_cost:
                print(
                    f"Skipping move {move} as it leads to an already visited state")
                continue

            # Calculate costs for the new state
            new_state.g_cost = new_g_cost
            new_state.h_cost = heuristic_manhattan(new_state.board)
            new_state.f_cost = new_state.g_cost + new_state.h_cost

            # Mark this state as visited and add it to the queue
            visited[new_board_str] = new_g_cost
            came_from[new_board_str] = (current_board_str, move)
            heapq.heappush(
                priority_queue, (new_state.f_cost, moves_count, new_state))
            print(
                f"Move {move} added to the queue with f_cost: {new_state.f_cost}")

        # Increment the move counter
        moves_count += 1
        print(f"Moves made so far: {moves_count}")

        # Stop if the number of moves exceeds a reasonable limit
        if moves_count >= 1000:
            print("\nExceeded maximum moves - puzzle might be unsolvable")
            return None

    print("\nNo solution found")
    return None


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
                # Fixed distance calculation
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance
