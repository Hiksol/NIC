import numpy as np
import random

def carve_passages_from(maze, x, y):
    maze[y, x] = 0
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 < nx < maze.shape[1] and 0 < ny < maze.shape[0] and maze[ny, nx] == 1:
            maze[y + dy//2, x + dx//2] = 0
            carve_passages_from(maze, nx, ny)

def generate_maze(width, height):
    if width % 2 == 0 or height % 2 == 0:
        raise ValueError("Width and height must be odd.")

    maze = np.ones((height, width), dtype=int)
    start = (1, 0)
    end = (height - 2, width - 1)

    maze[start[0], start[1]] = 0
    maze[end[0], end[1]] = 0

    carve_passages_from(maze, random.randrange(1, width, 2), random.randrange(1, height, 2))

    return maze

def save_mazes_to_file(filename, num_mazes, width, height):
    with open(filename, 'w') as file:
        for i in range(num_mazes):
            maze = generate_maze(width, height)
            for row in maze:
                file.write(" ".join(str(cell) for cell in row) + "\n")
            file.write("\n")

width, height = 11, 11
save_mazes_to_file("output", 100, width, height)
