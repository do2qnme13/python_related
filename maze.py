import sys


class Node():
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier= []

    def add(self,node):
        self.frontier.append(node)

    def contain_state(self,state):
        return any(node.state == state for node in self.frontier)    
    
    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1] # self.frontier.pop()
            return node
        


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:] # self.frontier.pop(0)
            return node
        


class Maze():

    def __init__(self,filename):
        
        # Read file and set height and width of Maze
        with open(filename,'r') as f:
            contents = f.read()

        # Check for start point and end point
        if contents.count('A') != 1 or  contents.count('B') != 1:
            raise Exception("Maze must contain exactly one start point 'A' and one goal 'B'")
        
        # Make 2D arrays
        self.maze = [list(line) for line in contents.splitlines()]


        self.walls = []
        for i,row in enumerate(self.maze):
            for j,cell in enumerate(row):
                if cell == 'A':
                    self.start = (i,j)
                elif cell == 'B':
                    self.goal = (i,j)
                elif cell == '#':
                    self.walls.append((i,j))



maze1 = Maze("maze1.txt")