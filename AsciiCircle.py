import sys
import math

#Constants
block = "#" #"█"
space = "." #" "
fill = False #True
radius = 25 #int(sys.argv[1])
useTrig = True
resolution = radius*100

#Create
gridSize = (radius*2) + 1
grid = [[space]*gridSize for x in range(gridSize)]

#Populate With Pythagoras
if useTrig:
    for i in range(resolution+1):
        x = (i/resolution) * radius
        y = math.sqrt(radius**2 - x**2)
        for dy in (-1, 1):
            for dx in (-1, 1):
                yCoord = radius + dy*int(round(y))
                xCoord = radius + dx*int(round(x))
                grid[yCoord][xCoord] = block
#Populate With Trigonometry
else:
    for i in range(-resolution, resolution):
        x = radius * math.sin((i/resolution)*2*math.pi) + radius
        y = radius * math.cos((i/resolution)*2*math.pi) + radius
        grid[round(y)][round(x)] = block


#Output 
print("")
for row in grid:
    for element in row:
        if fill:
            print(element*2, end="")
        else:
            print(element, end=" ")
    print("")
print("")