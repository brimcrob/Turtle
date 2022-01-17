import turtle


def stairs(size, nb):
    # forward 30 up 30 use for loops
    for i in range(0, nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    #     decrementing steps
    #     size = size - 10
    #     size -= 10
    t.forward(size)


t = turtle.Turtle()


def square(size, steps):
    for i in range(0, steps):
        t.forward(size)
        t.left(90)
        t.forward(size)


def squares(beginning_size, nb):
    for i in range(0, nb):
        size = (i + 1) * beginning_size
        square(size, 4)



# square(200, 4)
squares(10, 10)

# stairs(60, 5)

turtle.done()
