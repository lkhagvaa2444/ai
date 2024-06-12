import random
import math

# List of cities with coordinates (x, y)
cities = [
    (0, 3), (0, 0), (0, 2), (0, 1),
    (1, 0), (1, 3), (2, 0), (2, 3),
    (3, 0), (3, 3), (3, 1), (3, 2)
]

# Initial path (a simple circular path)
path = list(range(len(cities)))

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def path_length(path):
    dist = 0
    plen = len(path)
    for i in range(plen):
        dist += distance(cities[path[i]], cities[path[(i + 1) % plen]])
    return dist

def get_neighbors(path):
    neighbors = []
    plen = len(path)
    for i in range(plen):
        for j in range(i + 1, plen):
            neighbor = path[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climb(initial_path):
    current_path = initial_path[:]
    current_length = path_length(current_path)
    while True:
        neighbors = get_neighbors(current_path)
        best_neighbor = min(neighbors, key=path_length)
        best_length = path_length(best_neighbor)
        if best_length >= current_length:
            break
        current_path = best_neighbor
        current_length = best_length
    return current_path, current_length

# Run the hill climbing algorithm
initial_path = path[:]
print(f"Initial path: {initial_path}")
print(f"Initial path length: {path_length(initial_path)}")

optimal_path, optimal_length = hill_climb(initial_path)
print(f"Optimal path: {optimal_path}")
print(f"Optimal path length: {optimal_length}")
