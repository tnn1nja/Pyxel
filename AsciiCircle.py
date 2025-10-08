from math import sqrt

#Constants
block = "█"
space = " "
fill = True
radius = int(input("Enter your desired circle radius: "))

#Create
gridSize = (radius*2) + 1
grid = [[space]*gridSize for x in range(gridSize)]

#Populate
verts = radius*100
for i in range(verts+1):
    x = (i/verts) * radius
    y = sqrt(radius**2 - x**2)
    for dy in (-1, 1):
        for dx in (-1, 1):
            yCoord = radius + dy*int(round(y))
            xCoord = radius + dx*int(round(x))
            grid[yCoord][xCoord] = block

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