import turtle

wn = turtle.Screen()
wn.title('Recursive Circles!')
pointer = turtle.Turtle()
wn.bgcolor('white')
wn.setup(1200, 1200)

order = wn.numinput("Order Number", "Please Enter Order Number:", minval=1, maxval=10)

def koch(pointer, length, depth):
    if depth == 0:
        pointer.forward(length)
        return
    for angle in [60,360-120, 60]:
        koch(pointer, length / 3, depth - 1)
        pointer.right(angle)

    koch(pointer, length / 3, depth - 1)


def kochSnowFlake(pointer, length, depth):
    pointer.penup()
    pointer.setposition(-length / 2, 0)
    pointer.pendown()
    for i in range(3):
        koch(pointer, length, depth)
        pointer.left(120)

pointer.pencolor('black')
pointer.speed(0)

kochSnowFlake(pointer, 400, order)


wn.exitonclick()