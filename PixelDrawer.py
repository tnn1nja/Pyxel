import math

def getSymbols(debug):
    return ("#", ".") if debug else ("█", " ")

def getGrid(size, space):
    return  [[space]*size for x in range(size)]  

def drawGrid(grid, fillStretch=True):  
    print("")
    for row in grid:
        for element in row:
            if fillStretch:
                print(element*2, end="")
            else:
                print(element, end=" ")
        print("")
    print("")

def drawCircle(radius, debug=False, useTrig=True):
    block, space = getSymbols(debug)
    grid = getGrid(radius*2+1, space)
    resolution = radius*100
    
    if useTrig:
        for i in range(-resolution, resolution):
            x = radius * math.sin((i/resolution)*2*math.pi) + radius
            y = radius * math.cos((i/resolution)*2*math.pi) + radius
            grid[round(y)][round(x)] = block
    else:
        for i in range(resolution+1):
            x = (i/resolution) * radius
            y = math.sqrt(radius**2 - x**2)
            for dy in (-1, 1):
                for dx in (-1, 1):
                    yCoord = radius + dy*int(round(y))
                    xCoord = radius + dx*int(round(x))
                    grid[yCoord][xCoord] = block

    drawGrid(grid)

from sys import argv
drawCircle(int(argv[1]))