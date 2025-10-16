import math
debug = False
block, space = ("#", ".") if debug else ("█", " ")

def get_panel(width, height):
    return [[space]*width for x in range(height)]  

def display(panel):
    print("")
    for row in reversed(panel):
        for element in row:
            if debug: print(element, end=" ")
            else: print(element*2, end="")
        print("")
    print("")

def draw(panel, x, y):
    pass

def draw_line(panel, a, b, c, d):
    if c == a:
        return
    else:
        m = (b-d)/(a-c)
        iterations = round((abs(c-a)+1)*(abs(m)+1)*100)
        for i in range(iterations+1):
            x = min(a,c) + (i/iterations)*abs(c-a)
            y = m*x - m*a + b
            panel[round(y)][round(x)] = block

def display_circle(radius):
    resolution = radius*100

    panel = get_panel(radius*2+1, radius*2+1)
    for i in range(-resolution, resolution):
        x = radius * math.sin((i/resolution)*2*math.pi) + radius
        y = radius * math.cos((i/resolution)*2*math.pi) + radius
        panel[round(y)][round(x)] = block
    display(panel)

def displayTriangle(width, height=None):
    if height == None:
        height = width

    panel = get_panel(width, height)
    draw_line(panel, 0, 0, math.floor((width-1)/2), height-1)
    draw_line(panel, math.ceil(width-1)/2, height-1, width-1, 0)
    draw_line(panel, width-1, 0, 0, 0)
    display(panel)


if __name__ == "__main__":
    ()