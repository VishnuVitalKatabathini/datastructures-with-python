from collections import deque


def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    # Each state: (jug1, jug2)
    queue.append((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        # Print the state
        print(f"Jug1: {jug1}L, Jug2: {jug2}L")

        if jug1 == target or jug2 == target:
            print("Target achieved!")
            return True

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # All possible operations
        possible_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            # Pour jug1 -> jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour jug2 -> jug1
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)),
        ]

        for state in possible_states:
            if state not in visited:
                queue.append(state)

    print("Not possible to reach the target.")
    return False


# Example: Jug1 = 4L, Jug2 = 3L, Target = 2L
water_jug_bfs(5, 8, 4)
