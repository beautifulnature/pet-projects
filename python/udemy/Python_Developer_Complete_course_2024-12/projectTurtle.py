import turtle

# t.forward(100)
# t.left(90)
# t.forward(50)
# t.backward(100)
# t.right(45)
# t.forward(200)

def stairs(size, nb):
    for i in range(0, nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
        # size = size - 10
        # size -= 10
        # size = size + 10
        size += 10
    
    t.forward(size)

def square(side):
    for i in range(0, 4):
        t.forward(side)
        t.left(90)
        # side -= 1

def squares(beginning_size, nb):
    for i in range(0, nb):
        size = (i + 1) * beginning_size
        square(size)
        t.left(4)

t = turtle.Turtle()

# stairs(60, 5)
# square(100)
squares(10, 10)

turtle.done()