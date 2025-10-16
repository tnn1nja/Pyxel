import math
debug = True
block, space = ("#", ".") if debug else ("█", " ")

def get_radius_coords(radius, angle):
    x = radius + radius*math.sin(angle)
    y = radius + radius*math.cos(angle)
    return x, y

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
    if 0 <= x < len(panel[0]) and 0 <= y < len(panel):
        panel[y][x] = block

def draw_line(panel, a, b, c, d):
    if a == c:
        for y in range(round(min(b,d)), round(max(b,d))+1):
            draw(panel, a, y)
    else:
        m = (b-d)/(a-c)
        iterations = round((abs(c-a)+1)*len(panel))
        print(iterations)
        for i in range(iterations+1):
            x = min(a,c) + (i/iterations)*abs(c-a)
            y = m*x - m*a + b
            draw(panel, x , y)

def display_circle(radius):
    resolution = radius*100
    panel = get_panel(radius*2+1)
    for i in range(resolution):
        x, y = get_radius_coords(radius, (i/resolution)*2*math.pi)
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

def display_ngon(n, radius):
    panel = get_panel(radius*2+1)
    for i in range(n+1):
        x, y = get_radius_coords(radius, (i/n)*2*math.pi)
        if i > 0:
            draw_line(panel, lx, ly, x, y)
        lx, ly = x, y
    display_panel(panel)


if __name__ == "__main__":
    #display_ngon(6, 8)
    panel = get_panel(20, 20)
    draw_line(panel, 18.660254037844386, 15.0, 18.66025403784439, 5.00)
    display_panel(panel)
    ()

#18.660254037844386, 15.0, 18.66025403784439, 5.000000000000002