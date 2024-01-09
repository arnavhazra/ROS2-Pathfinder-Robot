
# gui.py

import tkinter as tk
from PIL import Image, ImageTk

class GridGUI:
    def __init__(self, grid):
        self.grid = grid
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.draw_grid()

    def draw_grid(self):
        # Implement logic to draw the grid, robot, and obstacles
        # Use self.canvas.create_rectangle() and self.canvas.create_oval() to draw the grid elements
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i, j] == 0:
                    self.canvas.create_rectangle(j * 10, i * 10, (j + 1) * 10, (i + 1) * 10, fill='white')
                else:
                    self.canvas.create_oval((j * 10 + 5, i * 10 + 5, (j * 10 + 9, i * 10 + 9), fill='black'))

        # Draw the robot and obstacles
        # You can use self.canvas.create_rectangle() and self.canvas.create_oval() to draw the robot and obstacles
        # For example, you can draw the robot at position (x, y) with radius 5 and color 'blue'
        # You can draw obstacles at positions (x, y) with radius 5 and color 'black'

    def update_grid(self, new_grid):
        # Update the grid and redraw the elements
        self.grid = new_grid
        self.draw_grid()

    def run_gui(self):
        self.root.mainloop()
