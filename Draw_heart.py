import turtle

with open("Detect_hands.py", "r") as file:
    detect_hands = file.read()
    
# Function to draw a heart shape.
def mini_draw_heart():
    turtle.pensize(3)
    turtle.goto(0,0)
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(18)
    turtle.circle(-10, 200)
    turtle.setheading(60)
    turtle.circle(-10, 200)
    turtle.forward(20)
    turtle.end_fill()

def draw_heart():
    turtle.down()
    turtle.color("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.setheading(60)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

def outline_draw_heart():
    turtle.goto(0,-130)
    turtle.setheading(0)
    turtle.pensize(3)

    turtle.down()
    turtle.color("black")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.setheading(60)
    turtle.circle(-90, 200)
    turtle.forward(180)

# Function to draw T Letter
def T_letter():
    turtle.color("red")
    turtle.goto(0, 0)
    turtle.setheading(180)
    turtle.forward(50);

    turtle.color("white")
    turtle.pensize(12)
    turtle.setheading(90)
    turtle.forward(50)
    
    turtle.setheading(180)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(50)

    # change position
    turtle.pensize(1)
    turtle.color("")
    turtle.goto(0,20)
    turtle.setheading(0)

    mini_draw_heart()

def M_letter():
    turtle.color("")
    turtle.setheading(0)
    turtle.forward(40)

    turtle.color("white")
    turtle.pensize(12)
    turtle.setheading(90)
    turtle.forward(50)

    turtle.setheading(315)
    turtle.forward(30)

    turtle.setheading(45)
    turtle.forward(30)

    turtle.setheading(-90)
    turtle.forward(50)
# Set up the turtle window.
turtle.bgcolor("white")
turtle.title("Top&Mina Love Forever")
turtle.color("white")
turtle.setup(500, 400)

# Start set up position
turtle.goto(0,-130)
turtle.speed(3)

# Draw the heart.
draw_heart()
outline_draw_heart()
# Draw T & M letter
T_letter() #--LO
M_letter() #--VE

turtle.hideturtle()
turtle.done()