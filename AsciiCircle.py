import math

def displayGrid(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print("")

radius = 5
gridSize = (radius*2) + 1
grid = [["."]*gridSize]*gridSize

displayGrid(grid)

x = 0
y = math.sqrt(radius**2 - x**2)
print(y)