from queue import Queue
from copy import deepcopy

# Goal state as 2D array
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def print_puzzle(state):
    """Print the 3x3 puzzle grid."""
    for row in state:
        print(row)
    print()

def find_blank(state):
    """Find the row and column of the blank tile (0)."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def get_next_states(state):
    """Get all possible next states by moving the blank tile."""
    row, col = find_blank(state)
    next_states = []
    
    # Possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:  # Check bounds
            # Create a deep copy of the state
            new_state = deepcopy(state)
            # Swap blank with adjacent tile
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            next_states.append(new_state)
    
    return next_states

def bfs_8_puzzle(start_state):
    """Solve the 8-puzzle using BFS."""
    queue = Queue()
    queue.put((start_state, []))  # (state, path)
    visited = set()
    visited.add(tuple(tuple(row) for row in start_state))  # Convert 2D list to tuple for hashing

    while not queue.empty():
        current_state, path = queue.get()
        
        if current_state == GOAL_STATE:
            return path + [current_state]
        
        for next_state in get_next_states(current_state):
            state_tuple = tuple(tuple(row) for row in next_state)
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.put((next_state, path + [current_state]))
    
    return None  # No solution found

def main():
    # Simple solvable initial state as 2D array
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    print("Initial state:")
    print_puzzle(initial_state)
    
    solution = bfs_8_puzzle(initial_state)
    
    if solution:
        print(f"Solution found in {len(solution)-1} moves:")
        for i, state in enumerate(solution):
            print(f"Step {i}:")
            print_puzzle(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()