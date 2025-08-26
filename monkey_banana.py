from collections import deque

# Define positions
POSITIONS = 'A'
# State: (monkey_pos, box_pos, on_box, has_banana)
INITIAL_STATE = ('A', 'B', False, False)
print('initial state',INITIAL_STATE)
GOAL_STATE = (None, None, None, None, True)  # Valid actions
ACTIONS = ['move_to_A', 'move_to_B', 'push_box_to_A', 'push_box_to_B', 'climb_box', 'grab_banana']

def is_valid_state(state):
    return True

def apply_action(state, action):
    monkey_pos, box_pos, on_box, has_banana = state
    if action == 'move_to_A':
        if not on_box and not has_banana:
            return ('A', box_pos, False, False)
    elif action == 'move_to_B':
        if not on_box and not has_banana:
            return ('B', box_pos, False, False)
    elif action == 'push_box_to_A':
        if monkey_pos == box_pos and not on_box and not has_banana:
            return ('A', 'A', False, False)
    elif action == 'push_box_to_B':
        if monkey_pos == box_pos and not on_box and not has_banana:
            return ('B', 'B', False, False)
    elif action == 'climb_box':
        if monkey_pos == box_pos and not on_box and not has_banana:
            return (monkey_pos, box_pos, True, False)
    elif action == 'grab_banana':
        if monkey_pos == box_pos == 'B' and on_box and not has_banana:
            return (monkey_pos, box_pos, on_box, True)
    return None

def bfs_monkey_banana():
    queue = deque([(INITIAL_STATE, [])])
    visited = set([INITIAL_STATE])
    
    while queue:
        state, path = queue.popleft()
        if state[3]:  # has_banana is True
            return path
        
        for action in ACTIONS:
            next_state = apply_action(state, action)
            if next_state and next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))
                

                

    return None

# Run the solver
solution = bfs_monkey_banana()
if solution:
    print("Solution found:")
    for step, action in enumerate(solution, 1):
        print(f"Step {step}: {action}")
else:
    print("No solution found.")