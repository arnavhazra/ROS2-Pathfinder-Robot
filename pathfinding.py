
#pathfinding.py

import numpy as np
from scipy.spatial import cKDTree

def a_star(grid, start, end):
    # Initialize start, end, and grid
    start, end = np.array(start), np.array(end)
    grid = np.array(grid)

    # Initialize heuristic, cost, and visited sets
    h = lambda x: sum(abs(i - j) for i, j in zip(x, end))
    cost = lambda x: sum(grid[x[0] + dx, x[1] + dy] == 0 for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)])
    visited = set()

    # Initialize open and closed sets
    open_set = {tuple(start)}
    closed_set = set()

    # Initialize current node and best path
    current_node = start
    best_path = [current_node]

    # Main loop
    while open_set:
        # Find the node with the lowest f-value in the open set
        current_node = np.array(min(open_set, key=lambda x: h(x) + cost(x)))

        # If the current node is the goal node, return the path
        if np.all(current_node == end):
            return best_path + [current_node]

        # Add the current node to the closed set
        closed_set.add(tuple(current_node))

        # Generate successors
        successors = [(current_node + move) for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        successors = [s for s in successors if np.all(s >= 0) and np.all(s < grid.shape)]

        # Update the open and closed sets
        open_set -= {tuple(current_node)}
        open_set.update([tuple(s) for s in successors if tuple(s) not in closed_set])

        # Update the best path
        best_path.append(current_node)

    return best_path

def visualize_path(grid, start, end, path):
    grid[start] = 2
    grid[end] = 2
    for node in path[1:-1]:
        grid[node] = 3
    visualize_grid(grid)