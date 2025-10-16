import math
debug = True
block, space = ("#", ".") if debug else ("█", " ")

def get_panel(width, height=None):
    if height == None:
        height = width

    return [[space]*width for x in range(height)]

def display_panel(panel):
    print("")
    for row in reversed(panel):
        for pixel in row:
            if debug: print(pixel, end=" ")
            else: print(pixel*2, end="")
        print("")
    print("")

def draw(panel, x, y):
    if x < len(panel) and x >= 0 and y < len(panel[0]) and y >= 0:
        panel[round(y)][round(x)] = block

def draw_line(panel, a, b, c, d):
    if a == c:
        for y in range(len(panel)):
            draw(panel, a, y)
    else:
        m = (b-d)/(a-c)
        iterations = round((abs(c-a)+1)*(abs(m)+1)*100)
        for i in range(iterations+1):
            x = min(a,c) + (i/iterations)*abs(c-a)
            y = m*x - m*a + b
            draw(panel, x , y)

def display_circle(radius):
    resolution = radius*100
    panel = get_panel(radius*2+1)
    for i in range(-resolution, resolution):
        x = radius * math.sin((i/resolution)*2*math.pi) + radius
        y = radius * math.cos((i/resolution)*2*math.pi) + radius
        draw(panel, x, y)
    display_panel(panel)

def display_triangle(width, height=None):
    if height == None:
        height = width

    panel = get_panel(width, height)
    draw_line(panel, 0, 0, math.floor((width-1)/2), height-1)
    draw_line(panel, math.ceil(width-1)/2, height-1, width-1, 0)
    draw_line(panel, width-1, 0, 0, 0)
    display_panel(panel)


if __name__ == "__main__":
    panel = get_panel(10)
    #draw_line(panel, 0, 9, 0, 0)
    #draw_line(panel, 0, 9, 9, 9)
    #draw_line(panel, 9, 9, 9, 0)
    #draw_line(panel, 9, 0, 0, 0)
    #draw_line(panel, 0, 0, 9, 9)
    #draw_line(panel, 9, 9, 0, 0)
    draw_line(panel, 0, 9, 0, 9)
    #currently vertical drawer always covers the entire panel
    display_panel(panel)
    ()