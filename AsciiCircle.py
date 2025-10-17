import math

def get_y(radius, x_center, y_center, x):
    return math.sqrt(radius**2 - (x_center - x)**2) + y_center

print(get_y(5, 1, 1, 5))