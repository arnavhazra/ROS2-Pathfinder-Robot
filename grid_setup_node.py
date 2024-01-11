import rclpy
from grid_environment import create_grid, set_obstacles, visualize_grid

def grid_setup_node():
    # Initialize ROS2 node
    node = rclpy.create_node('grid_setup')

    # Initialize grid, start, and end points
    grid = create_grid(10, 10)
    start = (2, 2)
    end = (7, 5)

    # Define obstacles
    obstacles = [(3, 3), (6, 6), (4, 4)]

    # Set obstacles in the grid
    grid = set_obstacles(grid, obstacles)

    # Visualize the grid
    visualize_grid(grid)