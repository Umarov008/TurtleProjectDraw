import turtle

draw_board =turtle.Screen()
draw_board.bgcolor("light green")
draw_board.title("Python Drawing")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
    #turtle_instance.right(10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+10)
    #turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

draw_board.listen()
draw_board.onkey(fun=turtle_forward,key="space")
draw_board.onkey(fun=rotate_angle_right,key="Down")
draw_board.onkey(fun=rotate_angle_left,key="Up")
draw_board.onkey(fun=clear_screen,key="c")
draw_board.onkey(fun=turtle_return_home,key="a")
draw_board.onkey(fun=turtle_pen_up,key="z")
draw_board.onkey(fun=turtle_pen_down,key="x")

turtle.mainloop()

