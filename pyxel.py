import math
import os

#Clear Terminal Window
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

#Convert Cooridinates from Polar to Cartesian
def polar_to_cartesian(radius, angle):
    x = radius + radius*math.sin(angle)
    y = radius + radius*math.cos(angle)
    return x, y

#Main Display Panel Class
class Panel:

    #Constructor
    def __init__(self, width, height=None):
        height = height if height else width
        self.panel = [[False]*width for x in range(height)]

    #Display Panel in Termainl
    def display(self, debug=False):
        if not debug:
            full_block = "\u2588"
            clear_console()
        for row in reversed(self.panel):
            for pixel in row:
                if debug:
                    print(("#" if pixel else "."), end=" ")
                else:
                    print((full_block if pixel else " ")*2, end="")
            print("")

    #Draw Single Pixel
    def draw(self, x, y): self.set_pixel(x, y, True)
    def erase(self, x, y): self.set_pixel(x, y, False)
    def set_pixel(self, x, y, value):
        if x % 1 != 0.5 and y % 1 != 0.5:
            x = round(x)
            y = round(y)
            if 0 <= x < len(self.panel[0]) and 0 <= y < len(self.panel):
                self.panel[y][x] = value
    
    #Draw Block of Pixels
    def fill(self, a, b, c, d): self.set_pixels(a, b, c, d, True)
    def clear(self, a, b, c, d): self.set_pixels(a, b, c, d, False)
    def set_pixels(self, a, b, c, d, value):
        a, c = sorted((a, c))
        b, d = sorted((b, d))
        for y in range(b, d+1):
            for x in range(a, c+1):
                self.set_pixel(x, y, value)

    #Draw Line
    def draw_line(self, a, b, c, d):
        a, c = sorted((a, c))
        b, d = sorted((b, d))
        if round(a,5) == round(c,5):
            for y in range(b), round(d+1):
                self.draw(a, y)
        else:
            m = (b-d)/(a-c)
            iterations = round(c-a+1)*len(self.panel)
            for i in range(iterations+1):
                x = a + (i/iterations)*c-a
                y = m*x - m*a + b
                self.draw(x , y)

    #Draw Simple Triangle
    def draw_triangle(self, a, b, width, height=None):
        if height == None:
            height = width
        self.draw_line(a, b, math.floor((width-1)/2)+a, height-1+b)
        self.draw_line(math.ceil((width-1)/2)+a, height-1+b, width-1+a, b)
        self.draw_line(width-1+a, b, a, b)

    #Draw Circle
    def draw_circle(self, a, b, radius):
        resolution = radius*100
        for i in range(resolution):
            x, y = polar_to_cartesian(radius, (i/resolution)*2*math.pi)
            self.draw(x+a, y+b)

    #Draw Regular Polygon
    def draw_regular_polygon(self, a, b, sides, radius):
        for i in range(sides+1):
            x, y = polar_to_cartesian(radius, (i/sides)*2*math.pi)
            if i > 0:
                self.draw_line(lx+a, ly+b, x+a, y+b)
            lx, ly = x, y