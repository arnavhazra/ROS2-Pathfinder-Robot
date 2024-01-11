
# robot_decision_making.py


class RobotDecisionMaking:
    def __init__(self, grid, start, end, path):
        self.grid = grid
        self.start = start
        self.end = end
        self.path = path

    def make_decision(self):
        def euclidean_distance(point1, point2):
            return sum([(i - j) ** 2 for i, j in zip(point1, point2)]) ** 0.5

        def heuristic_function(point1, point2):
            return euclidean_distance(point1, point2) + 10 * abs(point1[1] - point2[1])

        start_heuristic = heuristic_function(start, self.end)
        end_heuristic = heuristic_function(self.end, self.end)

        # Define the set of possible moves
        possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Define the best path as an empty list
        best_path = []

        # Define the current node as the start point
        current_node = start

        # Define the open set, closed set, and best path as empty sets
        open_set = set()
        closed_set = set()
        best_path = []

        # Add the start node to the open set
        open_set.add(tuple(start))

        # Main loop
        while open_set:
            # Find the node with the lowest f-value in the open set
            current_node = min(open_set, key=lambda x: heuristic_function(x, self.end) + cost(x))

            # If the current node is the goal node, return the path
            if current_node == self.end:
                return best_path + [current_node]

            # Add the current node to the closed set
            closed_set.add(tuple(current_node))

            # Generate successors
            successors = [(current_node + move) for move in possible_moves if self.is_valid_move(current_node + move)]

            # Update the open and closed sets
            open_set -= {tuple(current_node)}
            open_set.update(successors)

            # Update the best path
            if euclidean_distance(current_node, self.end) < euclidean_distance(self.end, current_node + move):
                best_path.append(current_node + move)

        return best_path
