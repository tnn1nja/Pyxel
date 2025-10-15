import math
debug = False
block, space = ("#", ".") if debug else ("█", " ")

def getGrid(width, height):
    return [[space]*width for x in range(height)]  

def drawGrid(grid):
    print("")
    for row in reversed(grid):
        for element in row:
            if debug: print(element, end=" ")
            else: print(element*2, end="")
        print("")
    print("")

def addLine(grid, a, b, c, d):
    if c == a:
        return 
    else:
        m = (b-d)/(a-c)
        iterations = round((abs(c-a)+1)*(abs(m)+1)*100)
        for i in range(iterations+1):
            x = min(a,c) + (i/iterations)*abs(c-a)
            y = m*x - m*a + b
            grid[round(y)][round(x)] = block

def drawCircle(radius):
    resolution = radius*100

    grid = getGrid(radius*2+1, radius*2+1)
    for i in range(-resolution, resolution):
        x = radius * math.sin((i/resolution)*2*math.pi) + radius
        y = radius * math.cos((i/resolution)*2*math.pi) + radius
        grid[round(y)][round(x)] = block
    drawGrid(grid)

def drawTriangle(width, height=None):
    if height == None:
        height = width

    grid = getGrid(width, height)
    addLine(grid, 0, 0, math.floor((width-1)/2), height-1)
    addLine(grid, math.ceil(width-1)/2, height-1, width-1, 0)
    addLine(grid, width-1, 0, 0, 0)
    drawGrid(grid)

if __name__ == "__main__":
    drawCircle(10)