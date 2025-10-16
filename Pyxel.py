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
    if x % 1 == 0.5 or y % 1 == 0.5:
        return
    
    x = round(x)
    y = round(y)
    if 0 <= x < len(panel[0]) and x >= 0 and 0 <= y < len(panel):
        panel[y][x] = block

def draw_line(panel, a, b, c, d):
    if a == c:
        for y in range(min(b,d), max(b,d)+1):
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
    display_panel(panel)
    ()