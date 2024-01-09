
#grid_environment.py

import numpy as np

def create_grid(width, height):
    grid = np.zeros((width, height))
    return grid

def set_obstacles(grid, obstacles):
    for obstacle in obstacles:
        x, y = obstacle
        grid[x, y] = 1
    return grid

def get_start_and_end(grid):
    start = None
    end = None
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == 0:
                if start is None:
                    start = (x, y)
                if end is None:
                    end = (x, y)
    return start, end

def visualize_grid(grid):
    import matplotlib.pyplot as plt
    plt.imshow(grid, cmap='gray')
    plt.show()