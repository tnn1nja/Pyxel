x = 5

def increase(): change(1)
def decrease(): change(-1)
def change(value):
    global x
    x += value

print(x)
increase()
print(x)