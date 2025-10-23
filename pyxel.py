import math
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def polar_to_cartesian(radius, angle):
    x = radius + radius*math.sin(angle)
    y = radius + radius*math.cos(angle)
    return x, y

class Panel:
    def __init__(self, width, height=None, debug=False):
        if height == None:
            height = width

        self.debug = debug
        self.panel = [[False]*width for x in range(height)]

    def display(self):
        if not self.debug:
            clear_console()
        for row in reversed(self.panel):
            for pixel in row:
                if self.debug:
                    print(("#" if pixel else "."), end=" ")
                else:
                    print(("\u2588" if pixel else " ")*2, end="")
            print("")

    def setPixel(self, x, y, value):
        if x % 1 == 0.5 or y % 1 == 0.5:
            return
        
        x = round(x)
        y = round(y)
        if 0 <= x < len(self.panel[0]) and 0 <= y < len(self.panel):
            self.panel[y][x] = value
    
    def draw(self, x, y):
        self.setPixel(x, y, True)
        
    def erase(self, x, y):
        self.setPixel(x, y, False)
        

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
        self.draw_line(math.ceil(width-1)/2+a, height-1+b, width-1, b)
        self.draw_line(width-1+a, b, a, b)

    def draw_circle(self, a, b, radius):
        resolution = radius*100
        for i in range(resolution):
            x, y = polar_to_cartesian(radius, (i/resolution)*2*math.pi)
            self.draw(x+a, y+b)

    def draw_ngon(self, a, b, n, radius):
        for i in range(n+1):
            x, y = polar_to_cartesian(radius, (i/n)*2*math.pi)
            if i > 0:
                self.draw_line(lx+a, ly+b, x+a, y+b)
            lx, ly = x, y


if __name__ == "__main__":
    pass