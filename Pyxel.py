import math

def polar_to_cartesian(radius, angle):
    x = radius + radius*math.sin(angle)
    y = radius + radius*math.cos(angle)
    return x, y

class Panel:
    stretch = True
    block = "█"
    space = " "
    panel = []

    def __init__(self, width, height=None, debug=False):
        if height == None:
            height = width
        if debug:
            self.block = "#"
            self.space = "."
            self.stretch = False
        self.panel = [[self.space]*width for x in range(height)]

    def display(self):
        print("")
        for row in reversed():
            for pixel in row:
                if self.stretch:
                    print(pixel, end=" ")
                else:
                    print(pixel*2, end="")
            print("")
        print("")

    def draw(self, x, y):
        if x % 1 == 0.5 or y % 1 == 0.5:
            return
        
        x = round(x)
        y = round(y)
        if 0 <= x < len(self.panel[0]) and 0 <= y < len(self.panel):
            self.panel[y][x] = self.block

    def draw_line(self, a, b, c, d):
        if round(a,5) == round(c,5):
            for y in range(round(min(b,d)), round(max(b,d))+1):
                self.draw(self.panel, a, y)
        else:
            m = (b-d)/(a-c)
            iterations = round((abs(c-a)+1)*len(panel))
            for i in range(iterations+1):
                x = min(a,c) + (i/iterations)*abs(c-a)
                y = m*x - m*a + b
                self.draw(self.panel, x , y)

    def draw_circle(self, radius, a=0, b=0):
        resolution = radius*100
        for i in range(resolution):
            x, y = polar_to_cartesian(radius, (i/resolution)*2*math.pi)
            self.draw(self.panel, x+a, y+b)

    def draw_triangle(self, width, height=None, a=0, b=0):
        if height == None:
            height = width
        self.draw_line(self.panel, a, b, math.floor((width-1)/2)+a, height-1+b)
        self.draw_line(self.panel, math.ceil(width-1)/2+a, height-1+b, width-1, b)
        self.draw_line(self.panel, width-1+a, b, a, b)

    def draw_ngon(self, n, radius, a=0, b=0):
        for i in range(n+1):
            x, y = polar_to_cartesian(radius, (i/n)*2*math.pi)
            if i > 0:
                self.draw_line(self.panel, lx+a, ly+b, x+a, y+b)
            lx, ly = x, y


if __name__ == "__main__":
    pass