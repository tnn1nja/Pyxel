import math
debug = False
block, space = ("#", ".") if debug else ("█", " ")

def getGrid(width, height):
    return [[space]*width for x in range(height)]  

def addLine(grid, a, b, c, d):
    m = (b-d)/(a-c)
    iterations = round((c-a)*m)
    for i in range(iterations):
        x = a + i/iterations
        y = m*a - m*a + b
        grid[round(y)][round(x)] = block

def drawGrid(grid):
    print("")
    for row in grid:
        for element in row:
            if debug:
                print(element, end=" ")
            else:
                print(element*2, end="")
        print("")
    print("")

def drawCircle(radius, useTrig=True):
    grid = getGrid(radius*2+1, radius*2+1)
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

grid = getGrid(10,10)
addLine(grid, 0, 0, 5, 10)
drawGrid(grid)