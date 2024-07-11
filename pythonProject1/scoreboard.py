from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("black")
        self.goto(-220, 240)
        self.hideturtle()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)

    def level(self):
        self.score += 1
        self.update_scoreboard()
