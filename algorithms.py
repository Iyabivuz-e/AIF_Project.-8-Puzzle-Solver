from collections import deque
import time

def breadth_first_search(initial_state):
    """
    Implement BFS to find the solution path
    Returns: (path, nodes_expanded, time_taken)
    """
    start_time = time.time()
    
    # Initialize the queue with initial state
    queue = deque([(initial_state, [])])  # Each element is (puzzle_state, path)
    visited = set()
    nodes_expanded = 0
    
    while queue:
        current_state, path = queue.popleft()
        nodes_expanded += 1
        
        # Check if we've reached the goal
        if current_state.is_goal_state():
            end_time = time.time()
            return path, nodes_expanded, end_time - start_time
            
        # Skip if we've seen this state
        if current_state in visited:
            continue
            
        visited.add(current_state)
        
        # Try all possible moves
        for move in current_state.get_possible_moves():
            new_state = current_state.clone()
            new_state.moving_agent(move)
            
            if new_state not in visited:
                queue.append((new_state, path + [move]))
    
    return None, nodes_expanded, time.time() - start_time

