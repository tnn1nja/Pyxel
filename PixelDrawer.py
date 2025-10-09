import math

def getSymbols(debug):
    if debug:
        return ("#", ".")
    else:
        return ("█", " ")

def getGrid(size, space):
    return  [[space]*size for x in range(size)]

def getTrigCircle(radius, debug=False):
    block, space = getSymbols(debug)
    grid = getGrid(radius*2+1)
    resolution = radius*10
    for i in range(-resolution, resolution):
        x = radius * math.sin((i/resolution)*2*math.pi) + radius
        y = radius * math.cos((i/resolution)*2*math.pi) + radius
        grid[round(y)][round(x)] = block
    return grid

def getPythCircle(radius, debug=False):
    block, space = getSymbols(debug)
    grid = getGrid(radius*2+1, space)
    resolution = radius*100
    for i in range(resolution+1):
        x = (i/resolution) * radius
        y = math.sqrt(radius**2 - x**2)
        for dy in (-1, 1):
            for dx in (-1, 1):
                yCoord = radius + dy*int(round(y))
                xCoord = radius + dx*int(round(x))
                grid[yCoord][xCoord] = block
    return grid

def drawGrid(grid, fillStretch):      
    print("")
    for row in grid:
        for element in row:
            if fillStretch:
                print(element*2, end="")
            else:
                print(element, end=" ")
        print("")
    print("")