# CTI 110




import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("P4LAB1")
screen.bgcolor("DarkSlateGray3")

t = turtle.Turtle()

t.color("DarkSeaGreen")
t.shape("turtle")
t.pencolor("DarkOrchid")
t.fillcolor("DeepPink4")
t.pensize(3)

sides = 4
angles = 360 / sides
length = 100

with t.fill():
    while sides > 0:
            t.forward(length)
            t.right(angles)
            sides = sides - 1

t.teleport(-200, 0)
sides = 4
t.begin_fill()
for side in range(sides):
    t.forward(length)
    t.right(angles)
t.end_fill()

sides = 3
t.fillcolor("BlueViolet")
t.begin_fill()
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(200, 180)
t.pendown()

COUNT = 120        # how many times the loop runs
LENGTH = 5         # length of the first line, in steps
TURN = 137         # degrees to turn left after each line
GROW = 2           # steps added to the length after each line
COLORS = ["#9D0208", "#DC2F02", "#F48C06", "#FFBA08"]

t.speed(0)         # 0 = fastest

# lines drawn = COUNT = 120
length = LENGTH
for i in range(COUNT):                     # one pass = one line
    t.pencolor(COLORS[i % len(COLORS)])    # pick the next color
    t.forward(length)
    t.left(TURN)
    length = length + GROW

t.hideturtle()
turtle.done() 