import math
debug = True
block, space = ("#", ".") if debug else ("█", " ")

def getGrid(width, height=None):
    if height == None:
        height = width
    return [[space]*width for x in range(height)]  

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

def addLine(grid, a, b, c, d):
    if c == a:
        return
    elif b == d:
        m = 0
    else:
        m = (b-d)/(a-c)

    iterations = round((abs(c-a)+1)*(abs(m)+1)*100)
    print(m)
    print(iterations)
    for i in range(iterations+1):
        x = min(a,c) + (i/iterations)*abs(c-a)
        y = m*x - m*a + b
        grid[round(y)][round(x)] = block
    print("\n")

def drawCircle(radius, useTrig=True):
    grid = getGrid(radius*2+1)
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

grid = getGrid(11)
addLine(grid, 5, 10, 0, 0)
drawGrid(grid)