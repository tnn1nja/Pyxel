import math
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def polar_to_cartesian(radius, angle):
    x = radius + radius*math.sin(angle)
    y = radius + radius*math.cos(angle)
    return x, y


class Panel:
    def __init__(self, width, height=None):
        height = height if height else width
        self.panel = [[False]*width for x in range(height)]

    def display(self, debug=False):
        if not debug:
            full_block = "\u2588"
            clear_console()
        for row in reversed(self.panel):
            for pixel in row:
                if debug: print(("#" if pixel else "."), end=" ")
                else:     print((full_block*2 if pixel else "  "), end="")
            print("")
    
    def draw(self, x, y): self.set_pixel(x, y, True)
    def erase(self, x, y): self.set_pixel(x, y, False)
    def set_pixel(self, x, y, value):
        panel_width = len(self.panel[0])
        panel_height = len(self.panel)
        if x % 1 != 0.5 and y % 1 != 0.5:
            x = round(x)
            y = round(y)
            if 0 <= x < panel_width and 0 <= y < panel_height:
                self.panel[y][x] = value
    
    def fill(self, a, b, c, d): self.set_pixels(a, b, c, d, True)
    def clear(self, a, b, c, d): self.set_pixels(a, b, c, d, False)
    def set_pixels(self, a, b, c, d, value):
        a, c = sorted((a, c))
        b, d = sorted((b, d))
        for y in range(b, d+1):
            for x in range(a, c+1):
                self.set_pixel(x, y, value)

    def draw_line(self, a, b, c, d):
        if round(a,5) == round(c,5):
            for y in range(round(min(b,d)), round(max(b,d))+1):
                self.draw(a, y)
        else:
            m = (b-d)/(a-c)
            iterations = round((abs(c-a)+1)*len(self.panel))
            for i in range(iterations+1):
                x = min(a,c) + (i/iterations)*abs(c-a)
                y = m*x - m*a + b
                self.draw(x , y)

    def draw_triangle(self, a, b, width, height=None):
        if height == None:
            height = width
        self.draw_line(a, b, math.floor((width-1)/2)+a, height-1+b)
        self.draw_line(math.ceil((width-1)/2)+a, height-1+b, width-1+a, b)
        self.draw_line(width-1+a, b, a, b)

    def draw_circle(self, a, b, radius):
        resolution = radius*100
        for i in range(resolution):
            x, y = polar_to_cartesian(radius, (i/resolution)*2*math.pi)
            self.draw(x+a, y+b)

    def draw_polygon(self, a, b, sides, radius):
        for i in range(sides+1):
            x, y = polar_to_cartesian(radius, (i/sides)*2*math.pi)
            if i > 0:
                self.draw_line(lx+a, ly+b, x+a, y+b)
            lx, ly = x, y