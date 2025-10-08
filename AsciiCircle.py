from math import sqrt

def display(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print("")

def create(radius):
    gridSize = (radius*2) + 1
    grid = [["."]*gridSize for x in range(gridSize)]

    verts = radius*10
    for i in range(verts+1):
        x = (i/verts) * radius
        y = sqrt(radius**2 - x**2)
        for dy in (-1, 1):
            for dx in (-1, 1):
                grid[radius + dy*int(round(y))][radius + dx*int(round(x))] = "#"
    
    return grid

display(create(5))