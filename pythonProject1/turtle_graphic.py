from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class TurtleGraphic(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.fd(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)