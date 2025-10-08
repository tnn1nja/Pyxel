from math import sqrt

#Constants
block ="#" #"█"
space = "." #" "
fill = False
radius = 5  #int(input("Enter your desired circle radius: "))

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

#Stretch
if fill:
    for row in grid:
        for i in range(len(row)):
            symbol = row[i*2]
            row.insert(i*2, symbol)
    spacer = ""
else:
    spacer = " "

#Output 
for row in grid:
    for element in row:
        print(element, end=spacer)
    print("")