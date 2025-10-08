from math import sqrt

def displayGrid(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print("")

def intRound(num):
    return int(round(num))

radius = 7
gridSize = (radius*2) + 1
grid = [["."]*gridSize for x in range(gridSize)]

verts = 90
for i in range(verts+1):
    x = (i/verts) * radius
    y = sqrt(radius**2 - x**2)
    grid[radius - intRound(y)][radius - intRound(x)] = "#"
    grid[radius - intRound(y)][radius + intRound(x)] = "#"
    grid[radius + intRound(y)][radius - intRound(x)] = "#"
    grid[radius + intRound(y)][radius + intRound(x)] = "#"

displayGrid(grid)

