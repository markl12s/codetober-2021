import turtle, random

#set up
pen = turtle.Turtle()
pen.color('black')
turtle.colormode(255)
pen.hideturtle()
pen.speed(0)

window = turtle.Screen()
window.bgcolor('white')

screen_x = 700
screen_y = 480

#archetecture
def random_color():
    rgb = []

    rgb.append(random.randint(0, 255))
    rgb.append(random.randint(0, 255))
    rgb.append(random.randint(0, 255))

    return rgb

def hexagon_right(rgb):
    pen.pencolor(rgb[0], rgb[1], rgb[2])
    pen.fillcolor(rgb[0], rgb[1], rgb[2])

    pen.begin_fill()

    for i in range(6):
        pen.right(60)
        pen.forward(50)

    pen.end_fill()

def hexagon_left(rgb):
    pen.pencolor(rgb[0], rgb[1], rgb[2])
    pen.fillcolor(rgb[0], rgb[1], rgb[2])

    pen.begin_fill()

    for i in range(6):
        pen.left(60)
        pen.forward(50)

    pen.end_fill()

def setup_hexagon_right():
    pen.up()

    pen.right(60)
    pen.forward(50)
    pen.left(60)
    pen.forward(50)

    pen.down()

def setup_hexagon_left():
    pen.up()

    pen.right(60)
    pen.forward(50)

    pen.down()

def offscreen(x, y):
    pen.up()
    pen.goto(x, y)
    pen.setheading(0)
    pen.down()

#execution
origin_x = pen.xcor()
origin_y = pen.ycor()

for i in range(3):
    pen.left(120)

    rgb = random_color()
    hexagon_right(rgb)

    window.update()

x = 0
last_move = 'left'

while True:
    if pen.xcor() >= screen_x + 50:
        offscreen(origin_x, origin_y)
    elif pen.xcor() <= -abs(screen_x) - 50:
        offscreen(origin_x, origin_y)

    if pen.ycor() >= screen_y + 50:
        offscreen(origin_x, origin_y)
    elif pen.ycor() <= -abs(screen_x) - 50:
        offscreen(origin_x, origin_y)

    x = random.randint(1,2)

    if x == 1:
        setup_hexagon_right()
        rgb = random_color()
        hexagon_right(rgb)

    else:
        setup_hexagon_left()
        rgb = random_color()
        hexagon_left(rgb)
