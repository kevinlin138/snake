from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score is: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(f"Score is: {self.score}", align=ALIGNMENT, font=FONT)

    def ate_food(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.color("White")
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
