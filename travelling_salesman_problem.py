import itertools

# Distance matrix: distances[i][j] is the distance from city i to city j
distances = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

def tsp_brute_force(distances):
    n = len(distances)
    cities = range(n)
    min_path = float('inf')
    best_route = []

    for perm in itertools.permutations(cities):
        cost = 0
        for i in range(n - 1):
            cost += distances[perm[i]][perm[i + 1]]
        cost += distances[perm[-1]][perm[0]]  # Return to start
        if cost < min_path:
            min_path = cost
            best_route = perm

    return min_path, best_route

cost, route = tsp_brute_force(distances)
print("Minimum Cost:", cost)
print("Best Route:", route + (route[0],))  # include return to start
