
#path_planning_node.py

import rclpy
import numpy as np
from pathfinding import a_star, visualize_path
from robot import Robot

def path_planning_node():
    # Initialize ROS2 node
    node = rclpy.create_node('path_planning')

    # Initialize grid, start, and end
    grid = np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
    start = (1, 1)
    end = (2, 2)

    # Define obstacles
    obstacles = [(1, 2)]

    # Set obstacles in the grid
    grid = set_obstacles(grid, obstacles)

    # Initialize robot
    robot = Robot(grid)
    robot.set_position(start)
    robot.obstacles = obstacles

    # Calculate path
    path = a_star(grid, start, end)

    # Visualize path
    visualize_path(grid, start, end, path)