from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.i=0
        self.color("white")
        self.penup()
        self.setpos(0, 260)
        self.write(f"Scoreboard:{self.i}", move=False, align="center", font=("Arial", 18, "normal"))
        self.hideturtle()

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 18, "normal"))

    def inc(self):
        self.clear()
        self.i += 1
        self.write(f"Scoreboard:{self.i}", move=False, align="center", font=("Arial", 18, "normal"))