class Robot:
    def __init__(self, grid):
        self.grid = grid
        self.position = None
        self.obstacles = []
        self.obstacle_avoidance_enabled = False

    def set_position(self, position):
        self.position = position

    def get_valid_moves(self):
        x, y = self.position
        valid_moves = [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        for obstacle in self.obstacles:
            if obstacle in valid_moves:
                valid_moves.remove(obstacle)
        return valid_moves

    def move(self, move):
        x, y = self.position
        new_x, new_y = x + move[0], y + move[1]
        if self.is_valid_move(new_x, new_y):
            self.position = new_x, new_y
            return True
        return False

    def is_valid_move(self, x, y):
        if 0 <= x < self.grid.shape and 0 <= y < self.grid.shape:
            return self.grid[x, y] == 0