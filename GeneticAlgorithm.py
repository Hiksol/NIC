import numpy as np
import random

def getMazesFromFile(filename):
    mazes = []
    with open(filename, "r") as file:
        l = []
        for line in file:
            line = line.strip()
            if line:
                l.append(line.split())
            else:
                if l:
                    mazes.append(l)
                    l = []
        if l:
            mazes.append(l)
    return np.array(mazes).copy()

class Specimen:
    def __init__(self, solution, fitness = 0):
        self.solution = solution
        self.fitness = fitness
        self.length = len(solution)

def initPopulation(maze, population_size):
    population = []
    sizes = maze.shape()
    for i in range(population_size):
        solution = []
        for j in range(sizes[0] * sizes[1]):
            solution.append(random.choice(['u', 'd', 'r', 'l']))
        population.append(Specimen(solution))
    return np.array(population).copy()

def fitness(maze, solution, start, finish) -> float:
    time = 0
    position = start
    for action in solution:
        time += 1
        if action == 'u':
            nextPosition = (position[0], position[1] + 1)
            if position[1] + 1 < len(maze) and maze[nextPosition] != '1':
                position = nextPosition
        elif action == 'd':
            nextPosition = (position[0], position[1] - 1)
            if position[1] > 0 and maze[nextPosition] != '1':
                position = nextPosition
        elif action == 'r':
            nextPosition = (position[0] + 1, position[1])
            if position[0] + 1 < len(maze.T) and maze[nextPosition] != '1':
                position = nextPosition
        elif action == 'l':
            nextPosition = (position[0] - 1, position[1])
            if position[0] > 0 and maze[nextPosition] != '1':
                position = nextPosition
        if position == finish:
            return 1.0/time
    return 0.0

def computeFitness(maze, population, start, finish):
    for individual in population:
        individual.fitness = fitness(maze, individual.solution, start, finish)
    return population.copy()

def crossover(specimenOne, specimenTwo) -> Specimen:
    newSolution = []
    for i in range(specimenOne.solution.length):
        newSolution.append(random.choice([specimenOne.solution[i], specimenTwo.solution[i]]))
    return Specimen(newSolution)

def mutation(specimen, mutationRate) -> Specimen:
    solution = []
    for i in range(specimen.length):
        if random(1) <= mutationRate:
            solution.append(random.choice(['u', 'd', 'r', 'l']))
        else:
            solution.append(specimen.solution[i])
    return Specimen(solution)

def epoch(maze, population_size):
    

def solveMaze(maze, population_size, epochs):
    bestOnes = []
    for i in epochs:

    return 0


mazes = getMazesFromFile("output")
# maze = mazes[0]
# size = round(len(maze) ** 0.5)
# if len(maze) == size ** 2:
#     maze.reshape(size, size)
# else:
#     print("Invalid size!", len(maze), "!=", size + **2)
#     break