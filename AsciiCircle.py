from math import sqrt

block = "█"

def display(grid):
    for row in grid:
        for element in row:
            print(element, end="")
        print("")

def create(radius):
    gridSize = (radius*2) + 1
    grid = [[" "]*gridSize for x in range(gridSize)]

    verts = radius*10
    for i in range(verts+1):
        x = (i/verts) * radius
        y = sqrt(radius**2 - x**2)
        for dy in (-1, 1):
            for dx in (-1, 1):
                yCoord = radius + dy*int(round(y))
                xCoord = radius + dx*int(round(x))
                grid[yCoord][xCoord] = block

    for row in grid:
        for i in range(len(row)):
            symbol = " "
            if row[i*2] == block:
                symbol = block
            row.insert(i*2+1, symbol)

    return grid

display(create(5))