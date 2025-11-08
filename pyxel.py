import math
import os

full_block = "\u2588"

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def polar_to_cartesian(radius, angle):
    x = radius + radius*math.sin(angle)
    y = radius + radius*math.cos(angle)
    return x, y


class Panel:
    def __init__(self, width, height=None):
        self.height = height if height else width
        self.width = width
        self.panel = [[False]*self.width for row in range(self.height)]

    def display(self, debug=False):
        if not debug: clear_console()
        for row in reversed(self.panel):
            for pixel in row:
                if debug: print(("#" if pixel else "."), end=" ")
                else:     print((full_block*2 if pixel else "  "), end="")
            print("")
    
    def draw(self, x, y): self.set_pixel(x, y, True)
    def erase(self, x, y): self.set_pixel(x, y, False)
    def set_pixel(self, x, y, value):
        if x % 1 != 0.5 and y % 1 != 0.5:
            x = round(x)
            y = round(y)
            if 0 <= x < self.width and 0 <= y < self.height:
                self.panel[y][x] = value
    
    def fill(self, a, b, c, d): self.set_pixels(a, b, c, d, True)
    def clear(self, a, b, c, d): self.set_pixels(a, b, c, d, False)
    def set_pixels(self, a, b, c, d, value):
        a, c = sorted((a, c))
        b, d = sorted((b, d))
        for y in range(round(b), round(d)+1):
            for x in range(round(a), round(c+1)):
                self.set_pixel(x, y, value)

    def draw_line(self, a, b, c, d):
        if round(a) == round(c):
            b, d = sorted((b, d))
            for y in range(round(b), round(d)+1):
                self.draw(a, y)
        else:
            gradient = (b-d)/(a-c)
            line_width = abs(a-c)
            iterations = round(line_width*max(1,abs(gradient)))
            for i in range(iterations+1):
                x = min(a,c) + (i/iterations)*line_width
                y = gradient*x - gradient*a + b
                self.draw(x, y)
    
    def draw_shape(self, a, b, vertices):
        previous_vertex = None
        for vertex in vertices:
            if previous_vertex:
                self.draw_line(a, b, previous_vertex[0], previous_vertex[1])

    def draw_triangle(self, a, b, width, height=None):
        if not height: height = width
        left_peak = math.floor((width-1)/2)
        right_peak = math.ceil((width-1)/2)
        right_edge = width-1
        top_edge = height-1
        self.draw_line(a, b, left_peak+a, top_edge+b)
        self.draw_line(right_peak+a, top_edge+b, right_edge+a, b)
        self.draw_line(right_edge+a, b, a, b)

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


if __name__ == "__main__":
    panel = Panel(25)
    panel.draw_polygon(0, 0, 6, 12)
    panel.display(True)