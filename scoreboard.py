from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Oopss! ", False, "center", FONT)
