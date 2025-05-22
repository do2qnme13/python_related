import sys
from PIL import Image, ImageDraw

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class Maze:
    def __init__(self, filename):
        # Read maze from file
        with open(filename, 'r') as f:
            contents = f.read()

        # Validate maze
        if contents.count('A') != 1 or contents.count('B') != 1:
            raise Exception("Maze must have exactly one start point 'A' and one goal 'B'.")

        # Parse maze into list
        self.maze = [list(line) for line in contents.splitlines()]
        self.height = len(self.maze)
        self.width = max(len(row) for row in self.maze)

        self.start = None
        self.goal = None
        self.walls = []

        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if cell == 'A':
                    self.start = (i, j)
                elif cell == 'B':
                    self.goal = (i, j)
                elif cell == '#':
                    self.walls.append((i, j))

        if self.start is None or self.goal is None:
            raise Exception("Maze must contain both a start point 'A' and goal 'B'.")

        self.solution = None
        self.num_explored = 0

    def print(self):
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if (i, j) == self.start:
                    print('A', end=' ')
                elif (i, j) == self.goal:
                    print('B', end=' ')
                elif self.solution and (i, j) in self.solution:
                    print('*', end=' ')
                elif (i, j) in self.walls:
                    print('▇', end=' ')
                else:
                    print(' ', end=' ')
            print()

    def neighbors(self, position):
        row, col = position
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and self.maze[r][c] != '#':
                result.append((action, (r, c)))
        return result

    def solve(self):
        from collections import deque
        start_node = Node(state=self.start, parent=None, action=None)
        frontier = deque()
        frontier.append(start_node)

        explored = set()

        while frontier:
            node = frontier.popleft()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = cells
                return

            explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not any(front.state == state for front in frontier) and state not in explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.append(child)

        raise Exception("No solution found.")

    def output_image(self, filename, show_solution=True):
        cell_size = 50
        cell_border = 2

        img = Image.new(
            "RGB",
            (self.width * cell_size, self.height * cell_size),
            "white"
        )
        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):
                top_left = (j * cell_size, i * cell_size)
                bottom_right = ((j + 1) * cell_size, (i + 1) * cell_size)

                fill = "white"
                if (i, j) in self.walls:
                    fill = "black"
                elif (i, j) == self.start:
                    fill = "green"
                elif (i, j) == self.goal:
                    fill = "red"
                elif show_solution and self.solution and (i, j) in self.solution:
                    fill = "blue"

                draw.rectangle([top_left, bottom_right], fill=fill)

        img.save(filename)

maze = Maze('maze3.txt')
maze.solve()
maze.print()
maze.output_image("solved_maze.png", show_solution=True)
